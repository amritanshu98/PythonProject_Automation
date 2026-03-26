import pytest
import requests

@pytest.fixture()
def create_token():
    print("Generating Token")
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {"username": "admin", "password": "password123"}

    response = requests.post(url = url, headers = headers, json = json_payload)
    token = response.json()["token"]
    print(token)
    return token

@pytest.fixture()
def create_booking_id():
    print("Creating Booking ID !!")
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
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

    response = requests.post(url = url, headers =headers, json = payload)
    booking_id = response.json()["bookingid"]
    assert response.status_code == 200
    print(booking_id)
    print(response.json())
    return booking_id



@pytest.fixture()
def launch_browser():
    print("Launching Browser")
    return "Chrome"

@pytest.fixture()
def close_browser():
    print("Closing Browser")
    return "Closed"