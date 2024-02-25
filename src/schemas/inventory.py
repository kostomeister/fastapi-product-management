from typing import Optional
from pydantic import BaseModel, ConfigDict


class InventoryBase(BaseModel):
    product_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)


class InventoryCreate(InventoryBase):
    pass


class Inventory(InventoryBase):
    id: int


class InventoryUpdate(BaseModel):
    product_id: Optional[int] = None
    quantity: Optional[int] = None
