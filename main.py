from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


from api.routes import router



app = FastAPI(
    title="AI Study Assistant API",
    description="Backend API for the AI Study Assistant",
    version="1.0.0"
)


app.include_router(
    router,
    prefix="/api"
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():

    return FileResponse("static/index.html")
        
