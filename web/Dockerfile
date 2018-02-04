FROM python:3

COPY . /app/web
WORKDIR /app/web

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
