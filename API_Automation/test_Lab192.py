import pytest
import requests

#Put Request
def test_put_request_positive(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+ str(create_booking_id)
    PUT_URL = base_url + base_path

    cookies = "token="+create_token
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookies}
    json_payload = {
        "firstname": "Prince",
        "lastname": "Singh",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-02-10",
            "checkout": "2026-03-02"
        },
        "additionalneeds": ["Breakfast", "Lunch", "Wifi"]
    }

    response = requests.put(url =PUT_URL, headers= headers, json= json_payload)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Prince"
    assert response.json()["lastname"] == "Singh"
    assert response.json()["totalprice"] == 111
    assert response.json()["depositpaid"] == True
    assert response.json()["bookingdates"]["checkin"] == "2026-02-10"
    assert response.json()["bookingdates"]["checkout"] == "2026-03-02"
    assert response.json()["additionalneeds"] == ["Breakfast", "Lunch", "Wifi"]
    print(response.json())


#Delete Request
def test_delete_request_positive(create_token, create_booking_id):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    DELETE_URL = base_url + base_path
    headers = {"Content-Type": "application/json",
               "Cookie": "token="+create_token}
    response = requests.delete(url=DELETE_URL, headers= headers)
    assert response.status_code == 201





#Patch Request
# def test_patch_request_positive(create_token, create_booking_id):
#     base_url = "https://restful-booker.herokuapp.com"
#     base_path = "/booking/"+ str(create_booking_id)
#     PATCH_URL = base_url + base_path
#
#     cookies = "token="+create_token
#     headers = {"Content-Type": "application/json",
#                "Accept": "application/json",
#                "Cookie": cookies}
#     json_payload = {
#         "firstname": "Lucky",
#         "lastname": "Sharma",
#     }
#
#     response = requests.patch(url =PATCH_URL, headers= headers, json= json_payload)
#     assert response.status_code == 200
#     assert response.json()["firstname"] == "Lucky"
#     assert response.json()["lastname"] == "Sharma"
#     print(response.json())
