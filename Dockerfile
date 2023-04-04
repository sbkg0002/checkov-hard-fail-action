FROM python:alpine

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY requirements.txt entrypoint.sh main.py config.yaml /
RUN apk add --update --no-cache libc-dev libffi-dev gcc &&\
  pip install --upgrade pip &&\
  pip install --requirement requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
