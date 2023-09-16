from flask_smorest import Blueprint,abort
from flask import request
from flask.views import MethodView
import uuid
from db import stores

blp=Blueprint("Stores", __name__, description="operations on stores.")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def put(self,store_id):
        store_data=request.get_json()          
        try:
            stores[store_id]["name"]=store_data["name"]
            return stores
        except KeyError:
            abort (404, message="Store Not found")
        

    def delete(self,store_id):
        try:
            del stores[store_id]
            return {"message":"store deleted"} 
        except KeyError:
            abort(404, message="Store Not Found.")
    
@blp.route("/store")
class Store(MethodView):
    def post(self):
        store_data=request.get_json()
        store_id=uuid.uuid4().hex
        store={**store_data}
        stores[store_id]=store
        return stores
    
    def get(self):
        return stores