FROM python:3-buster

# RUN apt update

WORKDIR /src

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app

COPY html_to_pdf .

EXPOSE 5000

CMD python app.py