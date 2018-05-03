#!/usr/bin/env bash
#bash <(curl -s https://raw.githubusercontent.com/amayatsky/shadowsocks-url-generator/master/generate-url.sh) /etc/shadowsocks-libev/config.json

if [ ! -f "$1" ]
then
  echo "Config file doesn't exist"
  exit 1
fi

server=`cat $1 | python -c 'import json,sys; print json.load(sys.stdin)["server"]'`
echo "Server: $server"
method=`cat $1 | python -c 'import json,sys; print json.load(sys.stdin)["method"]'`
echo "Method: $method"
password=`cat $1 | python -c 'import json,sys; print json.load(sys.stdin)["password"]'`
echo "Password: HIDDEN"
port=`cat $1 | python -c 'import json,sys; print json.load(sys.stdin)["server_port"]'`
echo "Port: $port"
url=$(printf "%s:%s@%s:%s" "$method" "$password" "$server" "$port" | base64)
echo "URL: ss://$url#$server"
