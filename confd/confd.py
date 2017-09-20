import etcd
import logging
import os

def obtener_servicios(servicios={}):
    modificado = False
    procesados = set()
    host = os.environ['ETCD_HOST']

    c = etcd.Client(host=host, port=2379, protocol='http')
    try:
        for s in c.get('/services').children:
            try:
                servicio_key = s.key.replace('/services/','')
                upstream_key = s.key + '/upstream'

                servidores = {}
                if servicio_key not in servicios:
                    print(f'Agregando {servicio_key}')
                    modificado = True
                else:
                    servidores = servicios[servicio_key]['servidores']
                    modificado = modificado | servicios[servicio_key]['modificado'] != s.modifiedIndex | servicios[servicio_key]['creado'] != s.createdIndex

                procesadas = set()
                try:
                    for server in c.get(upstream_key).children:
                        try:
                            snombre = server.key.replace(upstream_key+'/','')

                            if snombre not in servidores:
                                print(f'Agregando {servicio_key} --> {snombre}')
                                modificado = True
                            else:
                                modificado = modificado | servidores[snombre]['modificado'] != server.modifiedIndex | servidores[snombre]['creado'] != server.createdIndex

                            servidores[snombre] = {
                                'nombre': snombre,
                                'server': server.value,
                                'modificado': server.modifiedIndex,
                                'creado': server.createdIndex
                            }
                            procesadas.add(snombre)

                        except Exception as e1:
                            logging.exception(e1)

                except Exception as e2:
                    logging.exception(e2)

                ''' elimino los que ya no existen '''
                for d in [i for i in servidores.keys() if i not in procesadas]:
                    print(f'Eliminando {servicio_key} --> {d}')
                    modificado = True
                    del servidores[d]


                servicios[servicio_key] = {
                    'nombre': servicio_key,
                    'modificado': s.modifiedIndex,
                    'creado': s.createdIndex,
                    'url': c.get(s.key + '/location').value,
                    'servidores': servidores
                }
                procesados.add(servicio_key)

            except Exception as e3:
                logging.exception(e3)

    except Exception as e4:
        logging.exception(e4)

    ''' elimino los servicios que ya no existen '''
    for d in [i for i in servicios.keys() if i not in procesados]:
        print(f'Eliminando {servicio_key} --> {d}')
        modificado = True
        del servicios[d]

    return modificado
