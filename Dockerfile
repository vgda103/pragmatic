# python 3.9.0 버전 이미지를 선택
FROM python:3.11.9

# home 폴더 선택
WORKDIR /home/

# 깃허브의 레파지토리를 복사
RUN git clone https://github.com/vgda103/pragmatic.git

# 클론한 레포지토리 디렉토리로 작업 디렉토리 변경
WORKDIR /home/pragmatic/

# requirements.txt 목록에 있는 파이썬 모듈설치
RUN pip install -r requirements.txt

# .env 파일을 생성하고 환경 변수를 추가
RUN echo "SECRET_KEY=django-insecure-=c5ge!bti_vqhkqjr-3ii=b95ws9m9#nw6@r4p_ebz(^ezxm*g" > .env

# Django 데이터베이스 마이그레이션을 수행.
RUN python manage.py migrate

# 포트번호 설정
EXPOSE 8000

# RUN 과 CMD 차이
# RUN : 이미지가 생성 될때 실행된다
# CMD : Docker 컨테이너가 시작될때 실행된다.

# Django 서버 실행 명령어
CMD [ "pyhton", "manage.py", "runserver", "0.0.0.0:8000" ]