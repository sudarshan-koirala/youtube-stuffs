import os

from typing import Iterable
from langchain_core.documents import Document as LCDocument
from langchain.prompts import ChatPromptTemplate
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.schema.runnable import Runnable, RunnablePassthrough, RunnableConfig
from langchain.schema import StrOutputParser
from langchain.callbacks.base import BaseCallbackHandler

from qdrant_client import QdrantClient
#from langchain_groq import ChatGroq
from langchain_ollama import OllamaLLM
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaLLM
import chainlit as cl


# bring in our QDRANT_URL_LOCALHOST
from dotenv import load_dotenv
load_dotenv()


#groq_api_key = os.getenv("GROQ_API_KEY")
qdrant_url = os.getenv("QDRANT_URL_LOCALHOST")
client = QdrantClient(url=qdrant_url)

custom_prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

llm = OllamaLLM(
    model="deepseek-r1:latest"
)

#chat_model = ChatGroq(temperature=0, model_name="deepseek-r1-distill-llama-70b")

def format_docs(docs: Iterable[LCDocument]):
    return "\n\n".join(doc.page_content for doc in docs)


@cl.on_chat_start
async def on_chat_start():
    template = """Answer the question based only on the following context:

    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    def format_docs(docs):
        return "\n\n".join([d.page_content for d in docs])

    embeddings = FastEmbedEmbeddings()
    
    vectorstore = QdrantVectorStore.from_existing_collection(embedding=embeddings, collection_name="rag-llamaparse", url = qdrant_url)
    
    retriever = vectorstore.as_retriever()


    runnable = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    cl.user_session.set("runnable", runnable)
    
    
@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable
    msg = cl.Message(content="")

    class PostMessageHandler(BaseCallbackHandler):
        """
        Callback handler for handling the retriever and LLM processes.
        Used to post the sources of the retrieved documents as a Chainlit element.
        """

        def __init__(self, msg: cl.Message):
            BaseCallbackHandler.__init__(self)
            self.msg = msg
            self.sources = set()  # To store unique pairs

        def on_retriever_end(self, documents, *, run_id, parent_run_id, **kwargs):
            for d in documents:
                source_page_pair = (d.metadata['source'], d.metadata['page'])
                self.sources.add(source_page_pair)  # Add unique pairs to the set

        def on_llm_end(self, response, *, run_id, parent_run_id, **kwargs):
            if len(self.sources):
                sources_text = "\n".join([f"{source}#page={page}" for source, page in self.sources])
                self.msg.elements.append(
                    cl.Text(name="Sources", content=sources_text, display="inline")
                )

    async for chunk in runnable.astream(
        message.content,
        config=RunnableConfig(callbacks=[
            cl.LangchainCallbackHandler(),
            PostMessageHandler(msg)
        ]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
