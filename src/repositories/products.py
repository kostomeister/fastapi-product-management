from src.models.products import Product
from src.utils.repository import SQLAlchemyRepository


class ProductRepository(SQLAlchemyRepository):
    model = Product
