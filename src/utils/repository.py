from abc import ABC, abstractmethod

from sqlalchemy import select

from src.db.db import SessionLocal
from src.utils.validators import no_result_found_handler


class AbstractRepository(ABC):

    @abstractmethod
    async def get_one(self, id: int):
        pass

    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def create_one(self, data: dict):
        pass

    @abstractmethod
    async def update_one(self, id: int, data: dict):
        pass

    @abstractmethod
    async def delete_one(self, id: int):
        pass


class SQLAlchemyRepository(AbstractRepository):
    model = None

    @no_result_found_handler()
    async def get_one(self, id: int):
        async with SessionLocal() as db:
            query = select(self.model).where(self.model.id == id)
            result = await db.execute(query)
            return result.scalar_one()

    async def get_all(self):
        async with SessionLocal() as db:
            query = select(self.model)
            result = await db.execute(query)
            return result.scalars().all()

    async def create_one(self, data: dict):
        async with SessionLocal() as db:
            new_object = self.model(**data)
            db.add(new_object)
            await db.commit()
            return new_object

    @no_result_found_handler()
    async def update_one(self, id: int, data: dict):
        async with SessionLocal() as db:
            query = select(self.model).where(self.model.id == id)
            result = await db.execute(query)

            obj = result.scalar_one()
            for key, value in data.items():
                setattr(obj, key, value)
            await db.commit()
            return obj

    @no_result_found_handler()
    async def delete_one(self, id: int):
        async with SessionLocal() as db:
            query = select(self.model).where(self.model.id == id)
            result = await db.execute(query)
            obj = result.scalar_one()
            await db.delete(obj)
            await db.commit()
