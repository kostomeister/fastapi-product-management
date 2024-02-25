from src.repositories.inventory import InventoryRepository
from src.repositories.products import ProductRepository
from src.services.inventory import InventoryService
from src.services.products import ProductService


def get_product_service():
    return ProductService(ProductRepository)


def get_inventory_service():
    return InventoryService(InventoryRepository)
