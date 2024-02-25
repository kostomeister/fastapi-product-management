from datetime import datetime
from typing import Optional
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    description: str
    price: Decimal

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    created_at: datetime


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
