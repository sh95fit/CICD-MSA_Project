FROM python:latest

# tzdata 설치
RUN apk add --no-cache tzdata

# 시간대 설정 (예: Asia/Seoul)
ENV TZ=Asia/Seoul
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . /src
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install sqlalchemy pymysql

EXPOSE 8080

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "8080"]