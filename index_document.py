from app.services.ingestion_service import IngestionService

service = IngestionService()

service.ingest(
    "settings.UPLOAD_DIR/AI_ML_chart.pdf"
)