"""
    http://supervisord.org/api.html
"""
from xmlrpc.client import ServerProxy

def get_supervisor():
    return ServerProxy('http://127.0.0.1:9001/RPC2')

def reload_haproxy(s):
    s.supervisor.signalProcess('haproxy','TERM')
