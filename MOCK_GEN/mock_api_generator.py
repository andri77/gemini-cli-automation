import json

class MockApiGenerator:

    def __init__(self):
        self.data = {}

    def get(self, path, response_data, status_code=200):
        self.data[path] = {
            "GET": {
                "response_data": response_data,
                "status_code": status_code
            }
        }

    def post(self, path, response_data, status_code=201):
        self.data[path] = {
            "POST": {
                "response_data": response_data,
                "status_code": status_code
            }
        }

    def put(self, path, response_data, status_code=200):
        self.data[path] = {
            "PUT": {
                "response_data": response_data,
                "status_code": status_code
            }
        }

    def delete(self, path, status_code=204):
        self.data[path] = {
            "DELETE": {
                "status_code": status_code
            }
        }

    def generate(self):
        return json.dumps(self.data, indent=4)
