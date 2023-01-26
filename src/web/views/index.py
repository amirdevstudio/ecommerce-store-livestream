from fastapi import APIRouter
from fastapi.requests import Request

from src.web.views.templates import templates

index_router = APIRouter()

@index_router.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
