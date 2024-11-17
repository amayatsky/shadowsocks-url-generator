## Shadowsocks URL Generator [![Release](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Famayatsky%2Fshadowsocks-url-generator%2Freleases%2Flatest&query=%24.name&style=flat-square&label=Latest)](https://github.com/amayatsky/shadowsocks-url-generator/releases) [![Python](https://img.shields.io/badge/Python-3.9%2b-ffd343?style=flat-square)](https://www.python.org/downloads/) [![GithubActions](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Famayatsky%2Fshadowsocks-url-generator%2Fbadge%3Fref%3Dmaster&style=flat-square)](https://github.com/amayatsky/shadowsocks-url-generator/actions/) [![License](https://img.shields.io/badge/License-Apache%202.0-green?style=flat-square)](https://github.com/amayatsky/shadowsocks-url-generator/blob/master/LICENSE)

Python script that parses Shadowsocks server configuration file and generates a client configuration URI.

### Usage
Simply copy and paste the following in a terminal:
```bash
python <(curl -s https://raw.githubusercontent.com/amayatsky/shadowsocks-url-generator/master/ss-genuri.py) \
-c /etc/shadowsocks-libev/config.json
```
Change `/etc/shadowsocks-libev/config.json` path if needed. Alternatively, you can provide a different config file path

### Example
Input:
```json
{
    "remarks": "ShadowSocks Server",
    "server":"github.com",
    "server_port":8388,
    "password":"fake_pwd",
    "method":"chacha20-ietf-poly1305"
}
```
Output:
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmYWtlX3B3ZEBnaXRodWIuY29tOjgzODg=#ShadowSocks%20Server
```

### Requirements
Python 3.9+

### Contribution
Feel free to send your PRs and report any issues.

### Where to get the shadowsocks itself?
https://github.com/shadowsocks/shadowsocks-libev \
https://www.shadowsocks.org/en/index.html
