from flask_smorest import Blueprint,abort
from flask import request
from flask.views import MethodView
import uuid
from db import db
from resources.schemas import StoreSchema, StoreUpdateSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models.stores import StoreModel

blp=Blueprint("Stores", __name__, description="operations on stores.")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.arguments(StoreUpdateSchema)
    @blp.response(200, StoreSchema)
    def put(self,store_data,store_id):    
        store=StoreModel.query.get_or_404(store_id)
        try:
            if store_id:
                store.name=store_data["name"]
            db.session.add(store)
            db.session.commit()
        except SQLAlchemyError:
            abort (500,Message="Store Doesn't exists")
        return store
        

    def delete(self,store_id):
        try:
            store=StoreModel.query.get_or_404(store_id)
            db.session.delete(store)
            db.session.commit()
            return {"message":"Item Deleted Succesfully"}
        except SQLAlchemyError:
            abort (500,message="Deleting a store is not implemented.")
    
@blp.route("/store")
class Store(MethodView):
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self,store_data):
        store=StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A store with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the store.")
        return store
    
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        stores=StoreModel.query.all()
        return stores