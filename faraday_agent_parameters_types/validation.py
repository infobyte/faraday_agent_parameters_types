from faraday_agent_parameters_types.data_types import DATA_TYPE


def type_validate(p_type: str, data):
    if p_type not in DATA_TYPE:
        return [f"Invalid type: {p_type}"]
    schema = DATA_TYPE[p_type]
    errors = schema.validate({"data": data})
    return errors
