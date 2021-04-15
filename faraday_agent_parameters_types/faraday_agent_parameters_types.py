from marshmallow import Schema, post_load


class Type:
    def __init__(self, class_name):
        self.class_name = class_name
        self.value_dict = {}

    def __repr__(self):
        return self.class_name


class TypeSchema(Schema):
    @post_load
    def create_instance(self, data, **kwargs):
        return self._type(**data)

    def to_obj(self):
        return self._type().__str__()
