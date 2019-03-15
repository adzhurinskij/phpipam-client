# phpipam-client
PHPIPAM Python RESP API Client

![Travis (.org)](https://img.shields.io/travis/adzhurinskij/phpipam-client.svg)

It supports Python 2.7 and 3.4+.

__Example__
```python
from phpipam_client import PhpIpamClient

ipam = PhpIpamClient(
    url = 'https://ipam',
    app_id = 'myapp',
    username = 'mylogin',
    password = 'mypassword',
)

print(ipam.query('/sections/')
```

__Other API clients__
- https://github.com/adzhurinskij/phpipam-api-pythonclient (only Python 2.7)
- https://github.com/efenian/phpipamsdk
- https://github.com/michaelluich/phpIPAM
