from jinja2 import Environment, FileSystemLoader

def render_haproxy_cfg(services):
     env = Environment(loader=FileSystemLoader('templates'), trim_blocks=False)
     templ = env.get_template('haproxy.tmpl')
     outp = templ.render(services=services)
     with open('/tmp/haproxy.cfg','w') as f:
         f.write(outp)
