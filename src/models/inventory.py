from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.db.db import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id', ondelete="CASCADE"), unique=True)
    quantity: Mapped[int]

    product = relationship(
        "Product",
        back_populates="inventory",
        cascade="all, delete-orphan",
        single_parent=True
    )
