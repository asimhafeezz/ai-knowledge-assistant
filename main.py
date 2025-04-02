import os
import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.core import Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import chromadb
import tempfile

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

Settings.llm = OpenAI(model="gpt-4")
Settings.embed_model = OpenAIEmbedding()

CHROMA_PATH = "storage/chroma_db"
COLLECTION_NAME = "knowledge_base"

os.makedirs(CHROMA_PATH, exist_ok=True)

client = chromadb.PersistentClient(path=CHROMA_PATH)
chroma_collection = client.get_or_create_collection(name=COLLECTION_NAME)

vector_store = ChromaVectorStore(
    chroma_collection=chroma_collection
)

storage_context = StorageContext.from_defaults(vector_store=vector_store)

try:
    index = load_index_from_storage(storage_context)
except Exception as e:
    index = VectorStoreIndex.from_vector_store(vector_store)
    storage_context.persist()

st.set_page_config(page_title="AI Knowledge Base Assistant")
st.title("AI Knowledge Base Assistant")

if "file_indexed" not in st.session_state:
    st.session_state.file_indexed = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# upload section
uploaded_file = st.file_uploader("Upload a .pdf, .txt, or .md file", type=["pdf", "txt", "md"])

if uploaded_file and not st.session_state.file_indexed:
    with st.spinner("Indexing file..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
            tmp.write(uploaded_file.read())
            file_path = tmp.name

        reader = SimpleDirectoryReader(input_files=[file_path])
        docs = reader.load_data()

        for doc in docs:
            index.insert(doc)

        index.storage_context.persist()
        st.session_state.file_indexed = True
        st.success(f"'{uploaded_file.name}' has been indexed.")

# chat section
st.subheader("Ask a Question")
chat_container = st.container()

user_input = st.chat_input("Ask something about the document")

if user_input:
    with st.spinner("Thinking..."):
        try:
            query_engine = index.as_query_engine(similarity_top_k=5)
            response = query_engine.query(user_input)
            st.session_state.chat_history.append({"user": user_input, "bot": str(response)})
        except Exception as e:
            st.error(f"Error during query: {str(e)}")

# Show messages with latest at bottom (chat style)
with chat_container:
    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(chat["user"])
        with st.chat_message("assistant"):
            st.markdown(chat["bot"])