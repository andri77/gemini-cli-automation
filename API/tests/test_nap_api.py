import requests

NAP_API_URL = "https://www.nap.edu.au/naplan/public-demonstration-site"

def test_get_main_page():
    response = requests.get(NAP_API_URL)
    assert response.status_code == 200

def test_get_logo():
    response = requests.get("https://www.nap.edu.au/images/default-source/default-album/naplogo.jpg?sfvrsn=ea6c6a5e_4")
    assert response.status_code == 200
