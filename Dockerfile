FROM python:3.9-alpine3.14

RUN apk add --no-cache --update \
    ca-certificates \
    bash \
    curl 

ENV PYTHONUNBUFFERED=1
RUN ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x start.sh alive.sh

CMD [ "bash", "start.sh" ]