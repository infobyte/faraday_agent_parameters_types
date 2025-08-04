from dataclasses import dataclass, field

from marshmallow import fields, ValidationError, validates
import validators

from ..faraday_agent_parameters_types import TypeSchema


@dataclass
class FaradayDomainsList:
    data: list = field(default_factory=list)
    class_name: str = field(default="domains", init=False)
    base: str = field(default="list", init=False)


class FaradayDomainsListSchema(TypeSchema):
    data = fields.List(fields.Raw())
    type = FaradayDomainsList
    _composed = (str,)

    @validates("data")
    def validate_domain(self, items):
        for item in items:
            if not validators.domain(item):
                raise ValidationError("Item not a valid domain in list")
