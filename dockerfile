#FROM haproxy:1.7
FROM python:3.6.2-stretch
RUN apt-get update && apt-get install -y --no-install-recommends \
  supervisor \
  rsyslog \
  cron \
  nano \
  haproxy \
  lighttpd
  #&& apt-get clean \
  #&& rm -rf /var/lib/apt/lists/*

ENV TZ=America/Argentina/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY entrypoint.sh /
COPY lighttpd/lighttpd.conf /etc/lighttpd/
RUN mkdir /root/confd
ADD confd /root/confd
ADD supervisor/conf.d /etc/supervisor/conf.d

COPY requirements.txt /
RUN pip3 install -r requirements.txt

WORKDIR /root

ENTRYPOINT ["/entrypoint.sh"]
