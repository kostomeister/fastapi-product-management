from fastapi import HTTPException
from sqlalchemy import exc

from src.schemas.inventory import InventoryCreate, InventoryUpdate
from src.utils.repository import AbstractRepository


class InventoryService:
    def __init__(self, inventory_repo: AbstractRepository) -> None:
        self.inventory_repo: AbstractRepository = inventory_repo()

    async def add_inventory(self, inventory: InventoryCreate) -> None:
        try:
            if not await self.inventory_repo.product_exists(inventory.product_id):
                raise HTTPException(status_code=404, detail="No such product")
            inventory_dict = inventory.model_dump()
            inventory_obj = await self.inventory_repo.create_one(inventory_dict)
            return inventory_obj
        except exc.IntegrityError:
            raise HTTPException(status_code=404, detail="Inventory for this product already exists")

    async def get_inventory(self, id: int):
        return await self.inventory_repo.get_one(id)

    async def get_inventories(self):
        return await self.inventory_repo.get_all()

    async def delete_inventory(self, id: int):
        await self.inventory_repo.delete_one(id)
        return {"message": f"inventory with id {id} deleted successfully"}

    async def update_inventory(self, id: int, data: InventoryUpdate):
        inventory_dict = data.model_dump()
        return await self.inventory_repo.update_one(id, inventory_dict)
