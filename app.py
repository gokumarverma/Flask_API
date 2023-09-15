from flask import Flask
from flask_smorest import Api
from db import stores
from db import items
from resources.items import blp as ItemsBlueprint
from resources.stores import blp as StoresBlueprint

app=Flask(__name__)
if __name__=="__main__":
    app.run(debug=True)

app.config["PROPAGATE_EXCEPTIONS"]=True
app.config["API_TITLE"]="Stores REST API"
app.config["API_VERSION"]="v1"
app.config["OPENAPI_VERSION"]="3.0.3"
app.config["OPENAPI_URL_PREFIX"]="/"
app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"



api=Api(app)

api.register_blueprint(StoresBlueprint)
api.register_blueprint(ItemsBlueprint)   