from fastapi import APIRouter

from src.controllers.product import router as controllers_product

controllers_api_router = APIRouter()
controllers_api_router.include_router(controllers_product, prefix="/products")
