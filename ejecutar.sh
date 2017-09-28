#!/bin/bash
#sudo docker run -d --name haproxy -v $(pwd):/root -p 80:80 -p 1936:1936 haproxy
sudo docker run -d --name haproxy -p 80:80 -p 443:443 -p 1936:1936 -e ETCD_HOST=192.168.0.3 haproxy
sudo docker exec -ti haproxy bash
#sudo docker stop haproxy
#sudo docker rm haproxy

