import requests
import random
import time
import os

# Environment variables
BOX_TOKEN = os.getenv("BOX_TOKEN")
SENSOR_ID = os.getenv("SENSOR_ID")
RAD_SENSOR_ID = os.getenv("RAD_SENSOR_ID")
INTERVAL = int(os.getenv("INTERVAL", "30"))  # seconds between sends

API_URL = f"https://api.opensensemap.org/boxes/{BOX_TOKEN}/data"

def generate_value():
    return round(random.uniform(700.0, 3000.0), 2)

def generate_radiation_value():
    return round(random.uniform(0.30, 999999.0), 3)

def send_data():
    value = generate_value()
    ms_value = generate_radiation_value()
    payload = [
        {
            "sensor": SENSOR_ID,
            "value": value
        },
        {
            "sensor": RAD_SENSOR_ID,
            "value": ms_value
        }
    ]
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, json=payload, headers=headers)
    
    print(f"Status code: {response.status_code} - Response: {response.text}")
    print(f"Sent values -> Sensor1: {value}, Radiation: {ms_value} µSv/h")

if __name__ == "__main__":
    while True:
        try:
            send_data()
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(INTERVAL)