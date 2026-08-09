from fastapi import Request
from fastapi.responses import JSONResponse


class APIException(Exception):

    def __init__(self, message):

        self.message = message


async def api_exception_handler(
    request: Request,
    exc: APIException
):

    return JSONResponse(

        status_code=400,

        content={
            "error": exc.message
        }

    )