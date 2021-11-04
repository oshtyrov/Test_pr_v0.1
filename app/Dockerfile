FROM python:latest

WORKDIR /app

COPY ./ ./

RUN apt-get update && apt-get install -y python3-pip
RUN pip install -r requirements.txt
RUN chmod +x /app/get_data.py

CMD ["python3", "/app/get_data.py"]