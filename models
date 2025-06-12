class Item(BaseModel):
    name: str
    description: str

class ItemManager:
    def __init__(self):
        self.collection = collection

    async def add_item(self, item: Item):
        result = await self.collection.insert_one(item.dict())
        return {"message": "Item inserted", "id": str(result.inserted_id)}

    async def add_multiple_items(self, items: List[Item]):
        items_data = [item.dict() for item in items]
        result = await self.collection.insert_many(items_data)
        return {"message": "Items inserted", "ids": [str(id) for id in result.inserted_ids]}

item_manager = ItemManager()
