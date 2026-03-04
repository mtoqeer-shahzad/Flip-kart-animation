from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from flipkart.data_convertor import DataConvertor
from flipkart.config import Config

class DataIngestion:
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(
            model_name=Config.EMBEDDING_MODEL
        )
        self.vstore = AstraDBVectorStore(
            embedding=self.embedding,
            collection_name="flipkart_db",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE
        )

    def ingest(self, load_existing=True):
        if load_existing == True:
            return self.vstore

        docs = DataConvertor(
            r"D:\DJango\flipkart_product_recommender\data\flipkart_product_review.csv"
        ).convertor()

        self.vstore.add_documents(docs)
        return self.vstore


if __name__ == "__main__":
    ingestor = DataIngestion()
    ingestor.ingest(load_existing=False)