from fastapi import APIRouter

from src.web.views.index import index_router

router = APIRouter()
router.include_router(index_router)
