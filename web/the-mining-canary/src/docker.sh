#!/bin/bash
app="mining-canary"
docker build -t ${app} .
docker run -d -p 1180:80 --name=${app} -v $PWD:/app ${app}
