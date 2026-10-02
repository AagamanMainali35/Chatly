from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.config.settings import settings
from app.controller.auth import router as auth_routers
from app.controller.role import role_router
from app.controller.permission import permission_router
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.auth import decode_token
from fastapi import HTTPException

public_paths=[
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
        try:
            print(request.url.path)
            if request.url.path in public_paths:
                return await call_next(request)
            
            authorization = request.headers.get("Authorization")
            if not authorization:
                return JSONResponse(
                status_code=401,
                content={"detail": "Authorization token missing"},
            )
            parts=authorization.split()
            if len(parts)!=2 or parts[0]!="Bearer":
                return JSONResponse(
                status_code=401,
                content={"detail": "Invalid authorization header"},
                )
            token=parts[1]
            payload=decode_token(token)
            if not  payload['sub']:
                return JSONResponse(
                status_code=401,
                content={"detail": "Invalid authorization token provided"},
                )
            request.state.user_id=payload['sub']
            response = await call_next(request)
            return response
        except HTTPException as exc:
            return JSONResponse(status_code=400 , content={"details":exc.detail})

# #FastAPI initialization
# tags_metadata=[
#     {"name":"auth"},
#     {"name":"health"},
# ]
app=FastAPI()
# app.add_middleware(AuthMiddleware) # Add this middleware to the app to protect all routes except the public ones
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health",tags=["health"])
async def health():
    return JSONResponse(
        status_code=200,
        content="Up and running"
    )
    
app.include_router(auth_routers,tags=['auth'])
app.include_router(role_router,tags=['roles'])
app.include_router(permission_router,tags=['permissions'])