FROM python:3.10.4-alpine3.14

COPY . .

RUN apk add --no-cache --update \
    ca-certificates \
    bash \
    curl 

RUN chmod +x start.sh alive.sh

RUN python -m pip install -r requirements.txt

CMD [ "bash", "start.sh" ]