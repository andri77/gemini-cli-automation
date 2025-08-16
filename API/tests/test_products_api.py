import requests
import pytest

BASE_URL = "https://fakestoreapi.com/products"

# Positive Scenarios

def test_get_all_products():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_single_product():
    product_id = 1
    response = requests.get(f"{BASE_URL}/{product_id}")
    assert response.status_code == 200
    assert response.json()["id"] == product_id

def test_add_new_product():
    new_product_data = {
        "title": "test product",
        "price": 13.5,
        "description": "lorem ipsum dolor sit amet",
        "image": "https://i.pravatar.cc",
        "category": "electronic",
    }
    response = requests.post(BASE_URL, json=new_product_data)
    assert response.status_code == 201  # API returns 201 for successful creation
    assert response.json()["title"] == new_product_data["title"]

def test_update_product_put():
    product_id = 1
    updated_product_data = {
        "title": "updated product",
        "price": 20.0,
        "description": "updated description",
        "image": "https://i.pravatar.cc",
        "category": "clothing",
    }
    response = requests.put(f"{BASE_URL}/{product_id}", json=updated_product_data)
    assert response.status_code == 200
    assert response.json()["title"] == updated_product_data["title"]

def test_partially_update_product_patch():
    product_id = 1
    partial_update_data = {
        "price": 25.0
    }
    response = requests.patch(f"{BASE_URL}/{product_id}", json=partial_update_data)
    assert response.status_code == 200
    assert response.json()["price"] == partial_update_data["price"]

def test_delete_product():
    product_id = 1
    response = requests.delete(f"{BASE_URL}/{product_id}")
    assert response.status_code == 200
    assert response.json()["id"] == product_id

# Negative Scenarios

def test_get_non_existent_product():
    product_id = 99999
    response = requests.get(f"{BASE_URL}/{product_id}")
    assert response.status_code == 200

def test_add_product_with_invalid_data():
    invalid_product_data = {
        "title": "test product",
        "price": "invalid_price",  # Invalid data type
        "description": "lorem ipsum dolor sit amet",
        "image": "https://i.pravatar.cc",
        "category": "electronic",
    }
    response = requests.post(BASE_URL, json=invalid_product_data)
    assert response.status_code == 201  # Assuming API returns 201 even for invalid data

def test_update_non_existent_product():
    product_id = 99999
    updated_product_data = {
        "title": "updated product",
        "price": 20.0,
    }
    response = requests.put(f"{BASE_URL}/{product_id}", json=updated_product_data)
    assert response.status_code == 200

def test_delete_non_existent_product():
    product_id = 99999
    response = requests.delete(f"{BASE_URL}/{product_id}")
    assert response.status_code == 200
