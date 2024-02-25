from typing import List

from fastapi import Depends, APIRouter

from src.api.v1.dependencies import get_inventory_service
from src.schemas.inventory import Inventory, InventoryCreate, InventoryUpdate
from src.services.inventory import InventoryService


inventory_router = APIRouter(prefix="/api/v1/inventory")


@inventory_router.post("/")
async def create_inventory(inventory: InventoryCreate, inventory_service: InventoryService = Depends(get_inventory_service)):
    return await inventory_service.add_inventory(inventory)


@inventory_router.get("/{inventory_id}", response_model=Inventory)
async def get_inventory(inventory_id: int, inventory_service: InventoryService = Depends(get_inventory_service)):
    return await inventory_service.get_inventory(inventory_id)


@inventory_router.get("/", response_model=List[Inventory])
async def get_inventories(inventory_service: InventoryService = Depends(get_inventory_service)):
    return await inventory_service.get_inventories()


@inventory_router.patch("/{inventory_id}")
async def update_inventory(inventory_id: int, data: InventoryUpdate, inventory_service: InventoryService = Depends(get_inventory_service)):
    return await inventory_service.update_inventory(inventory_id, data)


@inventory_router.delete("/{inventory_id}")
async def delete_inventory(inventory_id: int, inventory_service: InventoryService = Depends(get_inventory_service)):
    return await inventory_service.delete_inventory(inventory_id)
