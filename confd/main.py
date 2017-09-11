#!/usr/local/bin/python
from pprint import pprint
import time
import logging
import shutil

import confd
import haproxy
import supervisor

if __name__ == '__main__':
    s = supervisor.get_supervisor()
    servicios = {}
    while True:
        try:
            modificado = confd.obtener_servicios(servicios)
            if modificado:
                pprint(servicios)
                haproxy.render_haproxy_cfg(servicios)
                shutil.copy('/tmp/haproxy.cfg','/etc/haproxy/')
                supervisor.reload_haproxy(s)
        except Exception as e:
            logging.exception(e)

        time.sleep(5)
