FROM python:3.13-slim:alpine

WORKDIR /app

COPY sensor_sim.py .

RUN pip install requests

CMD ["python", "sensor_sim.py"]