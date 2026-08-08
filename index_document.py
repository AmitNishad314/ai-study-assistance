from app.services.ingestion_service import IngestionService

service = IngestionService()

service.ingest(
    "storage/uploads/AI_ML_chart.pdf"
)