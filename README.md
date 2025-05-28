### Dockerized Sensor Simulation for openSenseMap

This project simulates IoT sensor data and sends it to [openSenseMap](https://opensensemap.org) using a Dockerized environment.

### What It Does

- **Simulates a senseBox** (a virtual environmental sensor station)
- **Sends periodic data** (e.g. temperature, humidity) to openSenseMap via its REST API
- **Runs inside a Docker container** for easy deployment and isolation
- Supports **environment variables** for authentication and configuration

### Components

- `Dockerfile`: Builds a lightweight container with a Python script for data simulation.
- `sensor_sim.py` Script that generates and posts random sensor data to your senseBox.

### Usage

```bash
docker build -t sensebox-simulator .
docker run -e BOX_TOKEN= \
           -e SENSOR_ID= \
           -e RAD_SENSOR_ID= \
           -e INTERVAL=30 \
           opensense-sensor
