FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
WORKDIR /var/www/app
COPY ./requirements.txt /var/www/requirements.txt
COPY ./app/static/ /var/www/app/static
RUN pip install -r /var/www/requirements.txt
