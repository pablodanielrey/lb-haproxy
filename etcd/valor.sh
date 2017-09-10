#!/bin/bash
curl http://127.0.0.1:2379/v2/keys/message -XPUT -d value="Hello world"
