FROM python:3.11-slim

WORKDIR /app

COPY sensor_sim.py .

RUN pip install requests

CMD ["python", "sensor_sim.py"]