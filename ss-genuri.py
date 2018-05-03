#!/usr/bin/env python
import argparse
import json
import base64

parser = argparse.ArgumentParser(description='A script that parses Shadowsocks server configuration file and generates '
                                             'a client configuration URI')
parser.add_argument('--config', '-c', type=str, default='/etc/shadowsocks-libev/config.json',
                    help='A path to your Shadowsocks server config.json')
args = parser.parse_args()

config = json.load(open(args.config))

uri = "%s:%s@%s:%d" % (
    config['method'],
    config['password'],
    config['server'],
    config['server_port'],
)

encoded_uri = base64.b64encode(uri.encode('utf-8'))
print('ss://%s' % encoded_uri.decode('utf-8'))
