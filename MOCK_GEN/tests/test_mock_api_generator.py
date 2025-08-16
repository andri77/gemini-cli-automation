import json
from MOCK_GEN.mock_api_generator import MockApiGenerator

def test_get_generator():
    generator = MockApiGenerator()
    generator.get("/users", {"users": [{"id": 1, "name": "John Doe"}]})
    expected_output = {
        "/users": {
            "GET": {
                "response_data": {"users": [{"id": 1, "name": "John Doe"}]},
                "status_code": 200
            }
        }
    }
    assert json.loads(generator.generate()) == expected_output

def test_post_generator():
    generator = MockApiGenerator()
    generator.post("/users", {"id": 2, "name": "Jane Doe"})
    expected_output = {
        "/users": {
            "POST": {
                "response_data": {"id": 2, "name": "Jane Doe"},
                "status_code": 201
            }
        }
    }
    assert json.loads(generator.generate()) == expected_output

def test_put_generator():
    generator = MockApiGenerator()
    generator.put("/users/1", {"id": 1, "name": "John Smith"})
    expected_output = {
        "/users/1": {
            "PUT": {
                "response_data": {"id": 1, "name": "John Smith"},
                "status_code": 200
            }
        }
    }
    assert json.loads(generator.generate()) == expected_output

def test_delete_generator():
    generator = MockApiGenerator()
    generator.delete("/users/1")
    expected_output = {
        "/users/1": {
            "DELETE": {
                "status_code": 204
            }
        }
    }
    assert json.loads(generator.generate()) == expected_output
