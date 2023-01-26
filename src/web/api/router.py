from fastapi import APIRouter

from src.web.api.v1.router import router as version_router

router = APIRouter(prefix='/api')
router.include_router(version_router)
