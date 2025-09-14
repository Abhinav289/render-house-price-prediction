

FROM python:3.11

WORKDIR /chpp_app

COPY . /chpp_app

RUN pip install -r requirements.txt

EXPOSE 5000


CMD ["python","./app.py"]

