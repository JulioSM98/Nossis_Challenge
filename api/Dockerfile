FROM python:3.8-slim-buster

RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/America/Buenos_Aires /etc/localtime

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh
COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt
COPY ./app /app
ENV PYTHONPATH=/app
WORKDIR /app
ENTRYPOINT [ "/start-reload.sh" ]
