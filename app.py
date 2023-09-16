from fastapi import FastAPI, Path , Query
from typing import Optional
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    name :str
    price:float
    brand: Optional[str] = None
class UpdateItem(BaseModel):
    name :Optional[str] = None
    price:Optional[float] = None
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

@app.put('/update-item/{item_id}')
def update_item(item_id : int , item:UpdateItem):
    if item_id not in inventory:
        return {"Error" : "Item not in inventory"}
    if item.name!= None:
        inventory[item_id].name = item.name
    if item.price!= None:
        inventory[item_id].price = item.price
    if item.brand!= None:
        inventory[item_id].brand = item.brand
    # inventory[item_id] = item
    return inventory[item_id]
# we have to manually update the items as the it is an instance of BaseModel and not an already made dictionary
# so now while updating if we only send one value then it will update only that element value and will not require you to specify all other element values

@app.delete('/delete-item')
def delete_item(item_id :int = Query(...,gt=0, description="The item_id you want to delete")):
    if item_id not in inventory:
        return {"Error" : "Item does not exist"}
    del inventory[item_id]
    return {"Success" : "Item deleted Successfully"}