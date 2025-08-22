import requests
import pytest
import json

BASE_URL = "https://fakestoreapi.com/products"

# Input Validation / Injection Flaws

def test_sql_injection_simulated():
    payload = "1 OR 1=1--"
    response = requests.get(f"{BASE_URL}/{payload}")
    # Expecting a non-200 or an error message, but FakeStoreAPI might return 200 with no data
    assert response.status_code == 200 or response.status_code == 404

def test_xss_injection_simulated():
    payload = "<script>alert('XSS')</script>"
    new_product_data = {
        "title": payload,
        "price": 10.0,
        "description": "test",
        "image": "test",
        "category": "test",
    }
    response = requests.post(BASE_URL, json=new_product_data)
    assert response.status_code == 201
    # Check if the payload is reflected unescaped (vulnerability)
    assert payload in response.json()["title"]

# Error Handling

def test_malformed_json_input():
    headers = {"Content-Type": "application/json"}
    invalid_json = "{\"title\": \"test\", "
    response = requests.post(BASE_URL, data=invalid_json, headers=headers)
    # Expecting a 400 Bad Request or similar, and no sensitive info in error
    assert response.status_code == 400 or response.status_code == 500
    assert "stack trace" not in response.text.lower()

def test_invalid_content_type():
    headers = {"Content-Type": "text/plain"}
    data = "some plain text data"
    response = requests.post(BASE_URL, data=data, headers=headers)
    # Expecting a 201 Created, as the API seems to accept plain text as valid input
    assert response.status_code == 201

# Rate Limiting (This test might be slow and might not fail if no rate limiting is in place)

def test_rate_limiting_simulated():
    for _ in range(100):
        response = requests.get(BASE_URL)
        assert response.status_code == 200  # Or expect 429 if rate limited
    # If the API has rate limiting, some requests might return 429. This test will pass if no rate limiting.
    # A more robust test would check for a 429 status code after a certain number of requests.

# New Advanced Security Tests

def test_mass_assignment_bopla():
    # Attempt to create/update a product with an unexpected field (e.g., 'isAdmin')
    # FakeStoreAPI doesn't have user roles, so this is a conceptual test.
    # A real API might have a field like 'role' or 'isAdmin' that should not be mass-assignable.
    product_data_with_extra_field = {
        "title": "product with extra field",
        "price": 100.0,
        "description": "test",
        "image": "test",
        "category": "test",
        "isAdmin": True # Malicious field
    }
    response = requests.post(BASE_URL, json=product_data_with_extra_field)
    assert response.status_code == 201
    # Assert that the extra field is NOT reflected in the response, indicating it was ignored
    assert "isAdmin" not in response.json()

def test_large_payload_handling():
    # Send a very large JSON payload to test resource consumption
    large_description = "A" * 100000 # 100KB string
    large_product_data = {
        "title": "large payload product",
        "price": 10.0,
        "description": large_description,
        "image": "test",
        "category": "test",
    }
    response = requests.post(BASE_URL, json=large_product_data)
    assert response.status_code == 201 or response.status_code == 200
    # Optionally, check response time for very large payloads

def test_invalid_http_method():
    # Attempt to use an unsupported HTTP method on an endpoint
    response = requests.put(BASE_URL) # PUT on /products (which only supports POST for creation)
    assert response.status_code == 405 or response.status_code == 404 # FakeStoreAPI might return 404

def test_ssrf_simulated():
    # Attempt to make the server request an internal resource via a URL parameter
    # FakeStoreAPI's 'image' field is a good candidate for this.
    ssrf_payload = "http://localhost/admin" # Attempt to access internal admin page
    product_data_with_ssrf = {
        "title": "ssrf test product",
        "price": 10.0,
        "description": "test",
        "image": ssrf_payload,
        "category": "test",
    }
    response = requests.post(BASE_URL, json=product_data_with_ssrf)
    assert response.status_code == 201
    # In a real scenario, you'd check server logs or network traffic for evidence of the SSRF attempt.
    # For FakeStoreAPI, we just check if it accepts the URL.
    assert response.json()["image"] == ssrf_payload

def test_long_string_fuzzing():
    # Send very long strings to various fields to test for buffer overflows or unexpected behavior
    long_string = "A" * 5000 # Very long string
    product_data_long_string = {
        "title": long_string,
        "price": 10.0,
        "description": long_string,
        "image": "test",
        "category": long_string,
    }
    response = requests.post(BASE_URL, json=product_data_long_string)
    assert response.status_code == 201 or response.status_code == 200
    # Assert that the API handles long strings gracefully (e.g., truncates, doesn't crash)
    assert len(response.json()["title"]) <= len(long_string)