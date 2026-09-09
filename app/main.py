from fastapi import FastAPI

from app.routes.auth import router as auth_router


app = FastAPI(
    title="BUZZ API",
    version="1.0.0"
)

app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"]
)
@app.get("/health", tags=["System"])
def health():
    return {"status": "ok"}