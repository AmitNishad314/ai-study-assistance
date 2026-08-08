from documents.pdf_reader import extract_pages,chunk_pages
from embeddings.gemini_embeddings import embed_chunks

from vector_store.faiss_store import FaissVectorStore
from vector_store.chroma_store import ChromaVectorStore


PDF_PATH = "storage/uploads/notes.pdf"


print("Extracting PDF...")

pages = extract_pages( PDF_PATH)


print("Chunking...")

chunks = chunk_pages(pages,"notes.pdf")


print(f"{len(chunks)} chunks created.")


print("Generating embeddings...")

embedded_chunks = embed_chunks(chunks)

print("Building chroma index...")

store = ChromaVectorStore()

store.add_chunks(embedded_chunks)

print("Index saved successfully.")