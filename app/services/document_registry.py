import json
import os

REGISTRY_FILE = "storage/document_registry.json"


class DocumentRegistry:
    def __init__(self):
        os.makedirs("storage", exist_ok=True)
        
        if not os.path.exists(REGISTRY_FILE):
            with open(REGISTRY_FILE, "w") as f:
                json.dump({}, f)
                
    def load(self):
        with open(REGISTRY_FILE, "r") as f:
            return json.load(f)
        
    def save(self):
        with open(REGISTRY_FILE, "w") as f:
            json.dump(self.documents, f, indent=4)
            
    def add_document(self, document):
        docs = self.load()
        docs.append(document)
        
        self.save()
        
    def list_documents(self):
        
        return self.load()
    
    def delete_document(self, document_id):
        
        docs = self.load()
        
        docs = [doc for doc in docs if doc["document_id"] != document_id]
        
        self.save()
        