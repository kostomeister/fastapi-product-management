from fastapi import FastAPI
from src.api.v1.inventory import inventory_router

from src.api.v1.products import products_router

app = FastAPI(description="FastAPI Product Management")

app.include_router(prefix="", router=products_router)
app.include_router(prefix="", router=inventory_router)
