FROM debian:lates
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./backend/utils /code/utils
COPY ./backend/tornado_main.py /code

ENTRYPOINT [ "python3", "tornado_main.py" ]