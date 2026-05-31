
### vpn_check.py

```python
#!/usr/bin/env python3

import socket
import sys


def check_host(host):
    try:
        ip = socket.gethostbyname(host)
        print(f"[+] {host} resolves to {ip}")
    except Exception as e:
        print(f"[-] Resolution failed: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vpn_check.py <hostname>")
        sys.exit(1)

    check_host(sys.argv[1])
