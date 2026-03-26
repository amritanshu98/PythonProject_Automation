import pytest
import allure
import requests

# base_url = "https://restful-booker.herokuapp.com"
# base_path = "/booking"
# URL = base_url + base_path

@allure.title("TC#1 - Create Booking CRUD")
@allure.description("TC#1 - Verify the Create Booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To make Request
    # URL
    # Method - POST
    # Headers - Content-type=Application/json
    # Payload / Data / Body - Dict / JSON
    # Auth(No)

    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    # URL = "https://restful-booker.herokuapp.com/booking"
    header = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Amrit",
        "lastname": "Kumar",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-02"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=header, json=payload)
    assert response.status_code == 200

    responseData = response.json()
    print(responseData)

    assert responseData["bookingid"] is not None
    assert type(responseData["bookingid"]) == int
    assert responseData["bookingid"] > 0

    # firstname = responseData["booking"]["firstname"]
    # assert firstname == "Amrit"

    assert responseData["booking"]["firstname"] != None
    assert responseData["booking"]["firstname"] == "Amrit"
    assert type(responseData["booking"]["firstname"]) == str
    assert responseData["booking"]["lastname"] != None
    assert responseData["booking"]["lastname"] == "Kumar"
    assert type(responseData["booking"]["lastname"]) == str
    assert responseData["booking"]["bookingdates"]["checkin"] == "2026-01-01"
    assert responseData["booking"]["bookingdates"]["checkout"] == "2026-01-02"
    assert responseData["booking"]["additionalneeds"] == "Breakfast"



@allure.title("TC#2 - Negative Create Booking CRUD")
@allure.description("TC#2 - Verify the Create Booking with payload {} - Empty Negative")
@pytest.mark.crud
def test_create_booking_negative_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {}

    response = requests.post(url=URL, headers=headers, json=json_payload)
    assert response.status_code == 500
    print(type(URL))
    print(type(headers))
    print(type(json_payload))



@allure.title("TC#3 - Negative Create Booking CRUD")
@allure.description("TC#3 - Verify the Create Booking with totalprice string Negative")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    header = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amrit",
        "lastname": "Kumar",
        "totalprice": "string",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-02"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=header, json=json_payload)
    assert response.status_code == 200


