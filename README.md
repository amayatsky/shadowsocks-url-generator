## Shadowsocks URL Generator
Python script that parses Shadowsocks server configuration file and generates a client configuration URI

### Usage
Simply copy and paste the following in a terminal:
```bash
python <(curl -s https://raw.githubusercontent.com/amayatsky/shadowsocks-url-generator/master/ss-genuri.py) \
-c /etc/shadowsocks-libev/config.json
```
Change /etc/shadowsocks-libev/config.json path if needed.

### Example
Input:
```javascript
{
    "server":"github.com",
    "server_port":8388,
    "password":"fake_pwd",
    "method":"chacha20-ietf-poly1305"
}
```
Output:
```bash
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpmYWtlX3B3ZEBnaXRodWIuY29tOjgzODg=
```

### Requirements
Python (compatible with both 2 and 3 interpeter versions)

### Contribution
Feel free to send your PRs and report any issues.

### Where to get the shadowsocks itself?
https://github.com/shadowsocks/shadowsocks-libev \
https://www.shadowsocks.org/en/index.html
