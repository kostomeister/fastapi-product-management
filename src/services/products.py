from src.schemas.products import ProductCreate, ProductUpdate
from src.utils.repository import AbstractRepository


class ProductService:
    def __init__(self, product_repo: AbstractRepository) -> None:
        self.product_repo: AbstractRepository = product_repo()

    async def add_product(self, product: ProductCreate) -> None:
        product_dict = product.model_dump()
        product_obj = await self.product_repo.create_one(product_dict)
        return product_obj

    async def get_product(self, id: int):
        return await self.product_repo.get_one(id)

    async def get_products(self):
        return await self.product_repo.get_all()

    async def delete_product(self, id: int):
        await self.product_repo.delete_one(id)
        return {"message": f"product with id {id} deleted successfully"}

    async def update_product(self, id: int, data: ProductUpdate):
        product_dict = data.model_dump()
        return await self.product_repo.update_one(id, product_dict)
