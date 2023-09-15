from fastapi import FastAPI, Path
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

@app.get("/get-by-name")
def get_item(name:str):
    for item_id in inventory :
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"DAta" : "Not found"}