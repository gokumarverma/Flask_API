from flask_smorest import Blueprint,abort
from flask import request
from flask.views import MethodView
import uuid
from db import items,stores
from resources.schemas import ItemSchema, ItemUpdateSchema

blp=Blueprint("Items", __name__, description="Operatioins on Items")

@blp.route("/items/<string:item_id>")
class Items(MethodView):
    @blp.arguments(ItemUpdateSchema)
    def put(self,item_data, item_id):
        try:
            item=items[item_id]
            item |=item_data
            return {"item":item}
        except KeyError:
            abort (404, message="Item Not Found")
    
    def delete(self,item_id):
        try:
            del items[item_id]
            return {"message":"item deleted succesfully"}
        except KeyError:
            abort (400, message="Item Not Found")
            
@blp.route("/items/<string:store_id>")        
class Items(MethodView):
    @blp.arguments(ItemSchema)
    def post(self,item_data,store_id):
        item_id=uuid.uuid4().hex
        if store_id in stores:
            item={"name":item_data["name"],"price":item_data["price"],"store_id":store_id }
            items[item_id]=item
            return {"Items":items}
        abort(404, message="Bad Request, store not found")


@blp.route("/items")
class Items(MethodView):
    def get(self):
        return {"items":items}
    