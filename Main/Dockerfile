FROM python:3.10-slim
RUN mkdir /cap
WORKDIR /cap
ADD . /cap
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
