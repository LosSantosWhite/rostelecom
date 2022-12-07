FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./backend/utils /code/utils
COPY ./backend/fastapi.py /code

ENTRYPOINT [ "uvicorn", "fastapi.py:app" ]