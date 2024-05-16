FROM python:3 # or python:3-slim, python:3-alpine or other suitable image

ADD app.py /

RUN pip3 install -r "requirements.txt"
CMD [ "python", "./app.py" ]