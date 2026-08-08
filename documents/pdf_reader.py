import fitz
from documents.chunker import chunk_text
from util.document_id import create_document_id



def extract_pages(pdf_path):

    document = fitz.open(pdf_path)

    pages=[]

    for page_number,page in enumerate(document.pages(),start=1):

        text = page.get_text()

        if text.strip():
            pages.append({
                "page_number": page_number,
                "text": text
            })
    
    document.close()

    return pages

def chunk_pages(pages,filename,chunk_size=1000, chunk_overlap=200):

    all_chunks=[]
    chunk_id=0
    

    for page in pages:
        page_chunks = chunk_text(page["text"],chunk_size,chunk_overlap)
        for text in page_chunks:
            document_id = create_document_id(filename, page["page_number"], chunk_id)
            all_chunks.append({
                "id": chunk_id,
                "text": text,
                "metadata": {
                    "document_id": document_id,
                    "filename": filename,
                    "page_number": page["page_number"]
                }
            })
            chunk_id+=1

    return all_chunks