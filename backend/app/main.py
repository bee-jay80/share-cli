from fastapi import FastAPI
from app.api.v1.routes import router as api_router

app = FastAPI(
    title="SwiftShare Backend",
    version="1.0.0",
    description="Backend API for the SwiftShare CLI file-sharing tool.",
)

# Register all v1 routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "SwiftShare backend is running!"}
