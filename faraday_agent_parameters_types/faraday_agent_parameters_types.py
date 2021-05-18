from marshmallow import Schema, post_load


class TypeSchema(Schema):
    @post_load
    def create_instance(self, data, **kwargs):
        return self._type(**data)

    def to_obj(self):
        return self._type().class_name
