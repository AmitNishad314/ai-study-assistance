import hashlib


def generate_document_id(filename: str):

    return hashlib.md5(
        filename.encode()
    ).hexdigest()