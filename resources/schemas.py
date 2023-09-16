from marshmallow import Schema, fields

class StoreSchema(Schema):
    id=fields.Str(dump_only=True)
    name=fields.Str(required=True)
    
class StoreUpdateSchema(Schema):
    name=fields.Str()
    
class ItemSchema(Schema):
    id=fields.Str(dump_only=True)
    name=fields.Str(required=True)
    price=fields.Float(required=True)
    
    
class ItemUpdateSchema(Schema):
    name=fields.Str()
    price=fields.Float()
    
