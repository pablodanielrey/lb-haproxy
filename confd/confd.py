import etcd

def obtener_servicios():
    servicios = []
    c = etcd.Client(host='192.168.0.3', port=2379, protocol='http')
    for s in c.get('/services').children:
        upstream_key = s.key + '/upstream'
        servicio_key = s.key.replace('/services/','')
        servicios.append({
            'nombre': servicio_key,
            'url': c.get(s.key + '/location').value,
            'servers': [ (i.key.replace(upstream_key+'/',''), i.value) for i in c.get(upstream_key).children ]
        })
    return servicios
