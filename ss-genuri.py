#!/usr/bin/env python
import argparse
import json
import base64

parser = argparse.ArgumentParser(description='A script that parses Shadowsocks server configuration file and generates '
                                             'a client configuration URI')
parser.add_argument('--config', '-c', type=str, help='A path to your Shadowsocks server config.json')

args = parser.parse_args()

if args.config is None:
    args.config='/etc/shadowsocks-libev/config.json'
    print('Using default config path: {}'.format(args.config))

config = json.load(open(args.config, 'r'))

uri = "%s:%s@%s:%d" % (
    config['method'],
    config['password'],
    config['server'],
    config['server_port'],
)

encoded_uri = base64.b64encode(uri.encode('utf-8')).decode('utf-8')

remarks = config.get('remarks', 'Shadowsocks Server')
remarks = "".join(remarks.split(' '))
print('ss://%s#%s' % (encoded_uri, remarks))
