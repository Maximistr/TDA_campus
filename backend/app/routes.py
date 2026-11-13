from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["api"])


@router.get("/v1/health")
def health_check():
    return {"status": "ok"}