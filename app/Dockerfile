FROM python:3.9 as builder
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM builder
WORKDIR /usr/src/app
COPY app.py app.py
COPY model.pkl model.pkl
ENV FLASK_APP=app

CMD [ "python", "app.py" ]
EXPOSE 5000

