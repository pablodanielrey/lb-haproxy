#!/bin/bash
sudo docker run \
	--rm -d \
	-p 2379:2379 \
	-p 2380:2380 \
	-p 4001:4001 \
	-p 7001:7001 \
	--name etcd \
	appcelerator/etcd:latest

