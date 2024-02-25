from typing import List

from fastapi import Depends, APIRouter

from src.api.v1.dependencies import get_product_service
from src.schemas.products import Product, ProductCreate, ProductUpdate
from src.services.products import ProductService


products_router = APIRouter(prefix="/api/v1/products")


@products_router.post("/")
async def create_product(product: ProductCreate, product_service: ProductService = Depends(get_product_service)):
    return await product_service.add_product(product)


@products_router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int, product_service: ProductService = Depends(get_product_service)):
    return await product_service.get_product(product_id)


@products_router.get("/", response_model=List[Product])
async def get_products(product_service: ProductService = Depends(get_product_service)):
    return await product_service.get_products()


@products_router.patch("/{product_id}")
async def update_product(product_id: int, data: ProductUpdate, product_service: ProductService = Depends(get_product_service)):
    return await product_service.update_product(product_id, data)


@products_router.delete("/{product_id}")
async def delete_product(product_id: int, product_service: ProductService = Depends(get_product_service)):
    return await product_service.delete_product(product_id)
