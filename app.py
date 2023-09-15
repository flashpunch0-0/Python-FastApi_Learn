from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()

inventory = {
    1: {
        "name" : "Milk",
        "Price" : 35,
        "Brand" : "amul"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path( description = "the id of the item you want to get from inventory")):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_item(*,item_id :int,name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"DAta" : "Not found"}