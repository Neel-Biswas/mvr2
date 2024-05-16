FROM python:3 # or python:3-slim, python:3-alpine or other suitable image

ADD app.py /

RUN pip3 install -r "https://github.com/Neel-Biswas/Movie_Recommend/blob/02114051931fc5fde6c541e7d4bfaef4e3ade8f6/requirements.txt"
CMD [ "python", "./app.py" ]