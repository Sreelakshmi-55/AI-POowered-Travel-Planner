import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

class TravelPlannerRAG:
    def __init__(self, index_path="faiss_index"):
        self.embeddings = OpenAIEmbeddings()
        # Load the pre-built vector database
        self.vector_store = FAISS.load_local(index_path, self.embeddings, allow_dangerous_deserialization=True)
        self.llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def get_itinerary(self, user_query):
        # Custom prompt to ensure structured, day-wise output
        template = """
        You are an expert travel assistant. Use the following pieces of retrieved context 
        to create a detailed, day-wise travel itinerary. 
        If the context doesn't contain enough info, use your general knowledge but flag it.
        
        User Request: {question}
        Context: {context}
        
        Structured Itinerary:
        """
        prompt = PromptTemplate(template=template, input_variables=["context", "question"])
        
        chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(search_kwargs={"k": 3}),
            chain_type_kwargs={"prompt": prompt}
        )
        
        return chain.invoke(user_query)