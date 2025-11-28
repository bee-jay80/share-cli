from fastapi import APIRouter

router = APIRouter()

# Simple health endpoint
@router.get("/health")
async def health_check():
    return {"status": "ok"}
