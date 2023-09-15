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
        for store in stores.values():
            if store["id"]==store_id:
                store["name"]=store_data["name"]
                return {"store":list(stores.values())}
        return {"message": "store not found"}
        

    def delete(self,store_id):
        for store in stores.values():
            if store["id"]== store_id:
                del stores[store_id]
                return {"message":"store deleted"} 
        return {"message":"store id not found"} 
    
@blp.route("/store")
class Store(MethodView):
    def post(self):
        store_data=request.get_json()
        store_id=uuid.uuid4().hex
        store={**store_data,"id":store_id}
        stores[store_id]=store
        return {"store":list(stores.values())}
    
    def get(self):
        return {"stores": list(stores.values())}