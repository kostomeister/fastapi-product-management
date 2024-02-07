from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, func, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.db.db import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str]
    price: Mapped[Decimal]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    inventory = relationship("Inventory", back_populates="product")
