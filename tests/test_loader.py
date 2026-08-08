from app.documents.pdf_loader import PDFLoader

loader = PDFLoader()

docs = loader.load(
    "storage/uploads/AI_ML_chart.pdf"
)

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)