FROM python:latest

COPY . /src
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install sqlalchemy pymysql

EXPOSE 8080

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8080"]