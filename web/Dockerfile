FROM python:3.6

COPY . /app/web
WORKDIR /app/web

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "-u", "app.py" ]
