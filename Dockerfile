FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY .env .
COPY . .

CMD ["python", "mm-bot.py"]
