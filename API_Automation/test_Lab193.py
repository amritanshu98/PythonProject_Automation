#Patch Request
import requests

def test_patch_request_positive(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+ str(create_booking_id)
    PATCH_URL = base_url + base_path

    cookies = "token="+create_token
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookies}
    json_payload = {
        "firstname": "Lucky",
        "lastname": "Sharma",
    }

    response = requests.patch(url =PATCH_URL, headers= headers, json= json_payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Lucky"
    assert response.json()["lastname"] == "Sharma"
    print(response.json())