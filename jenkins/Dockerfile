FROM jenkins/jenkins:lts

USER root

# Jenkins 외부의 서버에서 빌드가 완료된 서비스를 실행시켜야 하므로 SSH 접속 필요
RUN apt-get update &&\
  apt-get upgrade -y &&\
  apt-get install -y openssh-client
