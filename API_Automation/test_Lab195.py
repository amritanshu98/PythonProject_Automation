from dotenv import load_dotenv
import os

def test_update_request():
    load_dotenv()
    url = os.getenv("URL")
    print(url)
    username = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    print(username,"and", password)
