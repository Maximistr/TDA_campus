from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Python FastAPI Backend Template",
        description="A starter API for your application.",
    )

    # Allow a frontend dev server on another port (e.g. localhost:3000) to call the API.
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
    app.include_router(router)

    return app
