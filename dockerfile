FROM haproxy:1.7
RUN apt-get update && apt-get install -y \
  supervisor \
  rsyslog \
  cron \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Argentina/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY entrypoint.sh / 

RUN mkdir -p /etc/confd
RUN mkdir -p /etc/confd/conf.d
RUN mkdir -p /etc/confd/templates
COPY confd/conf.d/* /etc/confd/conf.d/
COPY confd/templates/* /etc/confd/templates/
RUN mkdir -p /opt/confd/bin
ADD confd /opt/confd/bin


ADD supervisor/conf.d /etc/supervisor/conf.d

#COPY haproxy/haproxy.cfg /usr/local/etc/haproxy/

WORKDIR /root

ENTRYPOINT ["/entrypoint.sh"]
