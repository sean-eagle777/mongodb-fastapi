from fastapi import FastAPI
from database import collection
from models import Item
from models import ItemManager
from bson import ObjectId
from typing import List

app = FastAPI()

item_manager = ItemManager()



@app.get("/SEAN")
async def read_data():
    data = await collection.find_one({"name": "example"})
    return data

@app.post("/")
async def add_item(item: Item):
    new_item = await collection.insert_one(item.dict())
    return {"message": "Item added", "id": str(new_item.inserted_id)}

@app.post("/add-item")
async def add_item(item: Item):
    return await item_manager.add_item(item)

@app.post("/add-items")
async def add_items(items: List[Item]):
    return await item_manager.add_multiple_items(items)

@app.delete("/{item_id}")
async def delete_item(item_id: str):
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 1:
        return {"message": "Item deleted"}
    else:
        return {"message": "Item not found"}
