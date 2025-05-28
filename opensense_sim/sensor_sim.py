import requests
import random
import time
import os

# Environment variables
BOX_TOKEN = os.getenv("BOX_TOKEN")
SENSOR_ID = os.getenv("SENSOR_ID")  # This is the sensor's ID, not the token
INTERVAL = int(os.getenv("INTERVAL", "30"))  # seconds between sends

API_URL = f"https://api.opensensemap.org/boxes/{BOX_TOKEN}/data"

def generate_value():
    return round(random.uniform(700.0, 3000.0), 2)

def send_data():
    value = generate_value()
    payload = [
        {
            "sensor": SENSOR_ID,
            "value": value
        }
    ]
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, json=payload, headers=headers)

    print(f"Sent value {value} - Status code: {response.status_code} - Response: {response.text}")

if __name__ == "__main__":
    while True:
        try:
            send_data()
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(INTERVAL)