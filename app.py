from flask import Flask, request
import uuid
from stores import stores
from items import items


app=Flask(__name__)
if __name__== "__main__":
    app.run(debug=True)

@app.get("/")
def get_stores():
    return {"stores": list(stores.values())}

@app.post("/store/addstore")
def create_store():
    store_data=request.get_json()
    store_id=uuid.uuid4().hex
    store={**store_data,"id":store_id}
    stores[store_id]=store
    return {"store":list(stores.values())}

@app.put("/store_update/<store_id>")
def update_store(store_id):
    new_store_data=request.get_json()
    for store in stores.values():
        if store["id"]==store_id:
            store["name"]=new_store_data["name"]
            return {"store":list(stores.values())}
    return {"message": "store not found"}
        
@app.delete("/store_delete/<store_id>")
def delete_store(store_id):
    for store in stores.values():
        if store["id"]== store_id:
            del stores[store_id]
            return {"message":"store deleted"} 
    return {"message":"store id not found"} 

@app.get("/items")
def get_all_items():
    return {"items":items}

@app.post("/additem/<store_id>")
def add_item(store_id):
    new_item=request.get_json()
    item_id=uuid.uuid4().hex
    for store in stores.values():
        if store["id"]==store_id:
            item={"name":new_item["name"],"price":new_item["price"],"store_id":store_id }
            items[item_id]=item
            return {"Items":items}
    return {"message":"store not found"}

@app.put("/update_item/<item_id>")
def update_item(item_id):
    try:
        item=items[item_id]
        item |=request.get_json()
        return {"item":item}
    except KeyError:
        return {"message":"item not found"}
            
@app.delete("/delete_item/<item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message":"item deleted succesfully"}
    except KeyError:
        return {"message":"item not found"}