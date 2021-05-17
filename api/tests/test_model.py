from api.model import Todo
import colander
from copy import deepcopy
import json
import pytest

TODO_DICT = {
        "id": 1,
        "done": False,
        "title": "test title",
        "description": "test description"
}

TODO = Todo()

def test_model_valid_input():
    serialized = TODO.serialize(TODO_DICT)
    assert isinstance(serialized, dict)
    json.dumps(serialized)
    
    deserialized = TODO.deserialize(serialized)
    assert isinstance(deserialized, dict)

    copy = deepcopy(TODO_DICT)
    copy.pop("id")

    deserialized = TODO.deserialize(copy)
    print(deserialized)



def test_model_invalid_input():
    for key, value in [("done", "not a boolean"), ("title", 1), ("description", 2)]:
        copy = deepcopy(TODO_DICT)
        copy[key] = value 
        
        with pytest.raises(colander.Invalid):
            #N.B - validation only takes place when deserializing data. No validation is performed upon serialization
            deserialized = TODO.deserialize(copy)

