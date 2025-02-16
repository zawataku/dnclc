FROM python:3.11

WORKDIR /app

COPY lib/dnclc.py /app/dnclc.py
COPY lib/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "/app/dnclc.py"]