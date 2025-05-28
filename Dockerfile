FROM python:3.13-alpine

WORKDIR /app

COPY opensense_sim/ .

RUN pip install requests

CMD ["python", "sensor_sim.py"]