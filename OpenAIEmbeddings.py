from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPEN_API_KEY"]=os.getenv("OPENAI_API_KEY")

#Convert Text into vectors
text = "This is lanchain practice and Open AI embaddings practice"
embaddings = OpenAIEmbeddings(model="text-embedding-3-large")

