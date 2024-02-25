from sqlalchemy import select

from src.db.db import SessionLocal
from src.models.inventory import Inventory
from src.utils.repository import SQLAlchemyRepository
from src.models.products import Product


class InventoryRepository(SQLAlchemyRepository):
    model = Inventory

    @staticmethod
    async def product_exists(product_id: int) -> bool:
        async with SessionLocal() as db:
            query = select(Product).filter(Product.id == product_id)
            result = await db.execute(query)
            product = result.scalar_one_or_none()
            return product is not None
