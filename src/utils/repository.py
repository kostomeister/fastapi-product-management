from abc import ABC, abstractmethod

from sqlalchemy import select

from src.db.db import SessionLocal


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
        print(data)
        async with SessionLocal() as db:
            new_object = self.model(**data)
            db.add(new_object)
            await db.commit()
            return new_object

    async def update_one(self, id: int, data: dict):
        async with SessionLocal() as db:
            query = select(self.model).where(self.model.id == id)
            result = await db.execute(query)
            obj = await result.fetchone()

            if obj:
                for key, value in data.items():
                    setattr(obj, key, value)
                await db.commit()
                return obj
            else:
                return None

    async def delete_one(self, id: int):
        async with SessionLocal() as db:
            query = select(self.model).where(self.model.id == id)
            result = await db.execute(query)
            obj = await result.fetchone()

            if obj:
                db.delete(obj)
                await db.commit()
            else:
                return None
