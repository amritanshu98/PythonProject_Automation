# To make a PUT request, we need
# URL
# New Booking
# Path - Booking ID
# Token - Auth
# Payload
import requests
import pytest
import allure


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {"username": "admin", "password": "password123"}

    response = requests.post(url = url, headers = headers, json = json_payload)
    token = response.json()["token"]
    print(token)
    return token

def create_booking():
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
    # print(response.json())
    return booking_id


def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+ str(create_booking())
    PUT_URL = base_url + base_path

    cookies = "token="+create_token()
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



def test_delete_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    DELETE_URL = base_url + base_path
    headers = {"Content-Type": "application/json",
               "Cookie": "token="+create_token()}
    response = requests.delete(url=DELETE_URL, headers= headers)
    assert response.status_code == 201






