from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.auth import decode_token
from fastapi import HTTPException
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health", tags=["health"])
async def health():
    return JSONResponse(
        status_code=200,
        content="Up and running"
    )

public_paths = [
    '/',
    '/docs',
    '/redoc',
    '/register',
    '/login',
    '/change-password',
    '/forget-password',
    "/openapi.json",
]

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path in public_paths:
            return await call_next(request)
        return await call_next(request)
