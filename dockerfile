FROM python:3.9-slim

WORKDIR /app/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

