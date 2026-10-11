from urllib.parse import quote

import httpx

from app.core.config import settings


SUPABASE_BUCKET = "MentorAI bucket"


class SupabaseStorage:
    def __init__(self):
        self.base_url = settings.SUPABASE_URL.rstrip("/")
        self.headers = {
            "apikey": settings.SUPABASE_SERVICE_ROLE_KEY,
            "Authorization": f"Bearer {settings.SUPABASE_SERVICE_ROLE_KEY}",
        }

    @staticmethod
    def document_path(document_id: str) -> str:
        return f"documents/{document_id}.pdf"

    def upload_pdf(self, path: str, content: bytes) -> None:
        bucket = quote(SUPABASE_BUCKET, safe="")
        object_path = quote(path, safe="/")
        headers = {
            **self.headers,
            "Content-Type": "application/pdf",
            "x-upsert": "false",
        }
        response = httpx.post(
            f"{self.base_url}/storage/v1/object/{bucket}/{object_path}",
            headers=headers,
            content=content,
            timeout=60,
        )
        response.raise_for_status()

    def delete_pdf(self, path: str) -> None:
        bucket = quote(SUPABASE_BUCKET, safe="")
        response = httpx.delete(
            f"{self.base_url}/storage/v1/object/{bucket}",
            headers=self.headers,
            json={"prefixes": [path]},
            timeout=60,
        )
        response.raise_for_status()
