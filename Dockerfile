FROM python:2.7.15-alpine3.7

EXPOSE 9999 

WORKDIR /usr/src/app

COPY ./app .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./hello.py" ]

