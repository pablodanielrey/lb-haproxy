#!/usr/local/bin/python

import confd
import haproxy
from pprint import pprint

if __name__ == '__main__':
    servicios = confd.obtener_servicios()
    pprint(servicios)
    haproxy.render_haproxy_cfg(servicios)
