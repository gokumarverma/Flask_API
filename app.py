from flask import Flask, request
import uuid
from stores import stores
from items import items


app=Flask(__name__)
if __name__== "__main__":
    app.run(debug=True)

@app.get("/")
def get_stores():
    return stores

@app.post("/store/addstore")
def create_store():
    store_data=request.get_json()
    store_id=uuid.uuid4().hex
    storetoadd={"name":store_data["name"], "id":store_id}
    stores.append(storetoadd)
    return storetoadd

@app.put("/store_update/<store_id>")
def update_store(store_id):
    new_store_data=request.get_json()
    for store in stores:
        if store["id"]==store_id:
            store["name"]=new_store_data["name"]
            return store
    return {"message": "store not found"}
        
@app.delete("/store_delete/<store_id>")
def delete_store(store_id):
    for store in stores:
        if store["id"]== store_id:
            stores.remove(store)
    return stores   

@app.get("/items")
def get_all_items():
    return items

@app.post("/additem/<store_id>")
def add_item(store_id):
    new_item=request.get_json()
    item_id=uuid.uuid4().hex
    for store in stores:
        if store["id"]==store_id:
            item={"name":new_item["name"],"price":new_item["price"],"id":item_id,"store_id":store_id }
            items.append(item)
            return item
    return {"message":"store not found"}

@app.put("/update_item/<item_id>")
def update_item(item_id):
    item_data=request.get_json()
    for item in items:
        if item["id"]==item_id:
            item["name"]=item_data["name"]
            item["price"]=item_data["price"]
            return item
    return {"message":"item not found"}
            
@app.delete("/delete_item/<item_id>")
def delete_item(item_id):
    for item in items:
        if item["id"]==item_id:
            items.remove(item)
            return {"message":"item deleted succesfully"}
    return {"message":"item not found"}