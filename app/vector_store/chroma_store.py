import chromadb
class ChromaVectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="storage/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )
    def add_chunks(self,embedded_chunks):
        ids = []

        documents = []

        embeddings = []

        metadatas = []
        
        for chunk in embedded_chunks:
             metadata = chunk["metadata"]
             
             chunk_id = f'{metadata["document_id"]}_{chunk["id"]}'
             
             ids.append(chunk_id)
             documents.append(chunk["text"])
             embeddings.append(chunk["embedding"])
             metadatas.append(metadata)
             
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )
        
    def search(self,query_embedding,top_k=5):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        formatted=[]
    
        for document,metadata,distance in zip(results['documents'][0],results['metadatas'][0],results['distances'][0]):
           formatted.append({
            "text": document,
            "metadata": metadata,
            "score": distance   
           })
        
        return formatted
    
    

    def count(self):

     return self.collection.count()
 
    def delete_document(self,document_id):
        self.collection.delete(
            ids=[document_id]
        )
        
    def get_all(self):
        return self.collection.get()

    
