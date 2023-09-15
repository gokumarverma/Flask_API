from flask_smorest import Blueprint,abort
from flask import request
from flask.views import MethodView
import uuid
from db import items,stores

blp=Blueprint("Items", __name__, description="Operatioins on Items")

@blp.route("/items/<string:item_id>")
class Items(MethodView):
    def put(self, item_id):
        try:
            item=items[item_id]
            item |=request.get_json()
            return {"item":item}
        except KeyError:
            return {"message":"item not found"}
    
    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message":"item deleted succesfully"}
        except KeyError:
            return {"message":"item not found"}
        
@blp.route("/items/<string:store_id>")        
class Items(MethodView):
    def post(self,store_id):
        new_item=request.get_json()
        item_id=uuid.uuid4().hex
        for store in stores.values():
            if store["id"]==store_id:
                item={"name":new_item["name"],"price":new_item["price"],"store_id":store_id }
                items[item_id]=item
                return {"Items":items}
        return {"message":"store not found"}

@blp.route("/items")
class Items(MethodView):
    def get(self):
        return {"items":items}
    