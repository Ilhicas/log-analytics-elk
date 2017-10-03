FROM alpine:3.5

RUN apk add --update alpine-sdk python python-dev py-pip tzdata libressl-dev libffi-dev build-base bash linux-headers

RUN rm -rf /var/cache/apk/*

COPY /app/requirements.txt /

RUN pip install -r requirements.txt

COPY /app/. /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]

