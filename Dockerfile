FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install pymongo[srv]
COPY . /code/
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
EXPOSE 8000/tcp