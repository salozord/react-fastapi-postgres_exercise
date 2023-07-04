from fastapi import FastAPI
import uvicorn

from core import config
from routes import offers as offers_routes

# Initializing the main app
app = FastAPI(title=config.BACK_NAME, docs_url="/api/docs", openapi_url="/api")

# Loading the routes
app.include_router(offers_routes.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host=config.BACK_HOST, reload=True, port=config.BACK_PORT)
