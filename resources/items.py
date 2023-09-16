from flask_smorest import Blueprint,abort
from flask import request
from flask.views import MethodView
from db import db
import uuid
#from db import items,stores
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from resources.schemas import ItemSchema, ItemUpdateSchema
from models.items import ItemModel
from models.stores import StoreModel

blp=Blueprint("Items", __name__, description="Operatioins on Items")

@blp.route("/items/<string:item_id>")
class Items(MethodView):
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item=ItemModel.query.get(item_id)
        if item:
            item.price= item_data["price"]
            item.name=item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()
        return item
    
    def delete(self,item_id):
        try:
            item=ItemModel.query.get(item_id)
            db.session.delete(item)
            db.session.commit()
            return {"message":"Item deleted Successfully"} ,200
        except SQLAlchemyError:
            abort (400, message="Item Doesn't exists")
        raise NotImplementedError("Deleting and item not implemented.")
            
@blp.route("/items/<string:store_id>")        
class Items(MethodView):
    @blp.arguments(ItemUpdateSchema)
    @blp.response(201, ItemSchema)
    def post(self,item_data,store_id):
        if StoreModel.query.get(store_id):
            try:
                item=ItemModel(**item_data,store_id=store_id)
                db.session.add(item)
                db.session.commit()
                return item
            except IntegrityError:
                abort(400, message="Item Already exists.")
            except SQLAlchemyError:
                abort(500, message="An error occured while adding item")
        abort(404, message="Store doesn't exists")
        


@blp.route("/items")
class Items(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        items=ItemModel.query.all()
        return items
    