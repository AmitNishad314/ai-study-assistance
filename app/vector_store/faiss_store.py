import json

import faiss
import numpy as np

class FaissVectorStore:

    def __init__(self):

        self.index = None
        self.chunks = []
        
    def add_chunks(self, embedded_chunks):
    

    
        if not embedded_chunks:
    
            return
    

    
        embeddings = np.array(
    
            [
    
                chunk["embedding"]
    
                for chunk in embedded_chunks
    
            ],
    
            dtype="float32"
    
        )
    

    
        faiss.normalize_L2(embeddings)
    

        dimension = embeddings.shape[1]
        if self.index is None:
           self.index = faiss.IndexFlatIP(dimension)
           
           
        self.index.add(embeddings)
    

    
        for chunk in embedded_chunks:
            
            self.chunks.append({
                {
    
                "id": chunk["id"],
    
                "text": chunk["text"],
    
                "metadata": chunk["metadata"]
    
            }
            })


    
    def search( self,query_embedding,top_k=3):
    
     results = self.collections.query(
        query_embeddings=[query_embedding],
        n_results=top_k
     )
     formatted =[]
    
     for document, metadata, distance in zip(
          results['documents'][0],
          results['metadatas'][0],
          results['distances'][0]
      ):
        formatted.append({
            "text": document,
            "metadata": metadata,
            "score": distance
        })
      
    

    
        return formatted
    

    
    def save(
    
        self,
    
        index_path="data/index.faiss",
    
        chunks_path="data/chunks.json"
    
    ):
    

    
        if self.index is None:
    
            raise ValueError(
    
                "No FAISS index to save."
    
            )
    

    
        faiss.write_index(
    
            self.index,
    
            index_path
    
        )
    

    
        with open(
    
            chunks_path,
    
            "w",
    
            encoding="utf-8"
    
        ) as file:
    

    
            json.dump(
    
                self.chunks,
    
                file,
    
                ensure_ascii=False,
    
                indent=2
    
            )


    
    def load(
    
        self,
    
        index_path="data/index.faiss",
    
        chunks_path="data/chunks.json"
    
    ):
    

    
        self.index = faiss.read_index(
    
            index_path
    
        )
    

    
        with open(
    
            chunks_path,
    
            "r",
    
            encoding="utf-8"
    
        ) as file:
    

    
            self.chunks = json.load(file)