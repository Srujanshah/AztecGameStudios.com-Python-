FROM python:latest
LABEL container_name flaskapp
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "__init__.py"]