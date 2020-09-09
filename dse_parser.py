class DSESchema:
    schema = {}

    def __init__(self):
        self.schema = dict()

    def propertyKey(self, key: str):
        prop = Property(key, self)
        return prop

    def add_property_key(self, key: str, prop: dict):
        self.schema[key] = prop


class Property:
    def __init__(self, name: str, schema: DSESchema):
        self.name = name
        self.schema = schema
        self.cardinality = "single"

    def _set_dtype(self, dtype: str):
        self.dtype = dtype

    def _set_cardinality(self, val: str):
        self.cardinality = val

    def single(self):
        self._set_cardinality("single")
        return self

    def multiple(self):
        self._set_cardinality("multiple")
        return self

    def ifNotExists(self):
        # ToDo: handle this condition
        return self

    def create(self):
        prop = {
            "type": self.dtype,
            "cardinality": self.cardinality
        }
        self.schema.add_property_key(self.name, prop)

    @classmethod
    def get_data_type_setter(cls, datatype: str):
        def set_data_type(self):
            self._set_dtype(datatype)
            return self
        return set_data_type


datatypes = ["text", "int", "timestamp"]


for dt in datatypes:
    setattr(Property, dt.title(), Property.get_data_type_setter(dt))
