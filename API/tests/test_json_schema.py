import requests
import pytest
from jsonschema import validate

BASE_URL = "https://fakestoreapi.com/products"

single_product_schema = {
    "type": "object",
    "required": ["id", "title", "price", "description", "category", "image"],
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "description": {"type": "string"},
        "category": {"type": "string"},
        "image": {"type": "string"},
        "rating": {
            "type": "object",
            "required": ["rate", "count"],
            "properties": {
                "rate": {"type": "number"},
                "count": {"type": "integer"}
            }
        }
    }
}

products_list_schema = {
    "type": "array",
    "items": {
        "$ref": "#/definitions/product"
    },
    "definitions": {
        "product": single_product_schema
    }
}

def test_get_all_products_schema():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    validate(instance=response.json(), schema=products_list_schema)

def test_get_single_product_schema():
    product_id = 1
    response = requests.get(f"{BASE_URL}/{product_id}")
    assert response.status_code == 200
    validate(instance=response.json(), schema=single_product_schema)

def test_add_new_product_schema():
    new_product_data = {
        "title": "test product",
        "price": 13.5,
        "description": "lorem ipsum dolor sit amet",
        "image": "https://i.pravatar.cc",
        "category": "electronic",
    }
    response = requests.post(BASE_URL, json=new_product_data)
    assert response.status_code == 201
    validate(instance=response.json(), schema=single_product_schema)
