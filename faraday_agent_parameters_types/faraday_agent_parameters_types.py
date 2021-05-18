from typing import Any
from marshmallow import Schema, post_load


class TypeSchema(Schema):

    # Overridden by data class values
    data: Any
    _type: Any

    @post_load
    def create_instance(self, data, **kwargs):
        return self._type(**data)

    def to_obj(self):
        return self._type().class_name
