from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    name :str
    price:float
    brand: Optional[str] = None
inventory = {}
# inventory = {
#     1: {
#         "name" : "Milk",
#         "Price" : 35,
#         "Brand" : "amul"
#     }
# }

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path( description = "the id of the item you want to get from inventory")):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_item(*,item_id :int,name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"DAta" : "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id : int, item: Item):
    if item_id in inventory:
        return {"Error ": "Item Id already exists"}
    # inventory[item_id] = {"name" : item.name , "brand":item.brand,  "price": item.price}
    inventory[item_id] = item
    return  inventory[item_id] 