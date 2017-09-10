#!/bin/bash
#
#  $1 -- nombre del servicio, ej: usuarios
#  $2 -- url del servicio, ej: /users
#  $3 -- nombre del servidor, ej: server1_v1
#  $4 -- ip:puerto del servidor, ej:  192.168.0.3:8000
#
#

curl http://127.0.0.1:2379/v2/keys/services/$1/location -XPUT -d value="$2"
curl http://127.0.0.1:2379/v2/keys/services/$1/upstream/"$3" -XPUT -d value="$4"
