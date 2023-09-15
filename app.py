from flask import Flask, request

app=Flask(__name__)
if __name__== "__main__":
    app.run(debug=True)


stores=[
    {
    "name":"vishal",
    "items":[
        {
            "name":"bed",
            "price":1800
        },
        {
            "name":"Coffee Machine",
            "price": 35000
        }
    ]
}
]


@app.get("/")
def get_stores():
    return stores

@app.post("/addstore")
def create_store():
    store_data=request.get_json()
    storetoadd={"name":store_data["name"], "item":[]}
    stores.append(storetoadd)
    return stores

@app.put("/<storename>")
def update_store(storename):
    new_store_data=request.get_json()
    for store in stores:
        if store["name"]==storename:
            store["name"]=new_store_data["name"]
            return stores
            
    return {"message": "store not found"}
        
@app.delete("/<storename>")
def delete_store(storename):
    for store in stores:
        if store["name"]== storename:
            stores.remove(store)
    return stores   

@app.get("/items/<storename>")
def get_store_items(storename):
    for store in stores:
        if store["name"]==storename:
            return {"Items":store["items"]}
            break
    return {"message":"store not found"}
            