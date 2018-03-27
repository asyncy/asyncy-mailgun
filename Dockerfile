FROM          jfloff/alpine-python:recent

COPY          app.py /app.py
RUN           pip install requests

ENTRYPOINT   ["python", "/app.py"]
