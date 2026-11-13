from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import initialize_database
from .routes import router


def create_app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        initialize_database()
        yield

    app = FastAPI(
        title="Python FastAPI Backend Template",
        description="A starter API for your application.",
        lifespan=lifespan,
    )

    # Allow a frontend dev server on another port (e.g. localhost:3000) to call the API.
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
    app.include_router(router)

    return app
