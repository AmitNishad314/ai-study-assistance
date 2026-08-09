from app.documents.pdf_loader import PDFLoader

loader = PDFLoader()

docs = loader.load(
    "settings.UPLOAD_DIR/AI_ML_chart.pdf"
)

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)