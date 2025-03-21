from datetime import datetime
from typing import List
from uuid import UUID

import pymongo
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.database import db_client
from src.models.product import ProductModel
from src.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from src.utils.exceptions import InsertionException, NotFoundException, UpdateException


class ProductUsecase:
    def __init__(self, collection=None) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        if collection:
            self.collection = collection
        else:
            self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        try:
            # Lógica para inserir o produto no banco de dados
            product = ProductModel(**body.dict())
            await self.collection.insert_one(product.dict())
            return ProductOut(**product.dict())
        except Exception as e:
            raise InsertionException(f"Failed to insert product: {str(e)}")

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductOut(**result)

    async def query(self) -> List[ProductOut]:
        return [ProductOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False

    async def patch(self, product_id: str, updates: dict) -> dict:
        # Busca o produto pelo ID
        product = await self.collection.find_one({"id": product_id})
        if not product:
            raise NotFoundException(f"Product with ID {product_id} not found")

        # Atualiza o campo updated_at com o horário atual
        updates["updated_at"] = datetime.utcnow()

        # Atualiza o produto no banco de dados
        result = await self.collection.update_one({"id": product_id}, {"$set": updates})
        if result.modified_count == 0:
            raise UpdateException("Failed to update product")

        # Retorna o produto atualizado
        updated_product = await self.collection.find_one({"id": product_id})
        if not updated_product:
            raise NotFoundException(f"Updated product with ID {product_id} not found")
        return updated_product


product_usecase = ProductUsecase()
