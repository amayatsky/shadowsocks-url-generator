#!/usr/bin/env python3
import argparse
import json
import base64
from pathlib import Path
from urllib.parse import quote

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='A script that parses Shadowsocks server configuration file and generates a client configuration URI'
    )
    parser.add_argument(
        '--config', '-c', 
        type=str, 
        help='A path to your Shadowsocks server config.json', 
        default='/etc/shadowsocks-libev/config.json'
    )
    return parser.parse_args()

def load_config(config_path: str) -> dict:
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_file, 'r') as file:
        return json.load(file)

def generate_ss_uri(config: dict) -> str:
    uri = f"{config['method']}:{config['password']}@{config['server']}:{config['server_port']}"
    encoded_uri = base64.b64encode(uri.encode('utf-8')).decode('utf-8')

    remarks = config.get('remarks', 'Shadowsocks Server')
    encoded_remarks = quote(remarks)

    return f'ss://{encoded_uri}#{encoded_remarks}'

def main():
    args = parse_arguments()
    config = load_config(args.config)
    ss_uri = generate_ss_uri(config)
    print(ss_uri)

if __name__ == '__main__':
    main()
