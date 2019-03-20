# phpipam-client
![Pyup Status](https://pyup.io/repos/github/adzhurinskij/phpipam-client/shield.svg) ![Travis (.org)](https://img.shields.io/travis/adzhurinskij/phpipam-client.svg)

PHPIPAM Python RESP API Client. It supports Python 2.7 and 3.4+.

### Example
Basic usage:
```python
from phpipam_client import PhpIpamClient, PATCH

ipam = PhpIpamClient(
    url='https://ipam',
    app_id='myapp',
    username='mylogin',
    password='mypassword',
    user_agent='myapiclient', # custom user-agent header
)

# read object
print(ipam.query('/sections/'))

# update object
ipam.query('/sections/1/', method=PATCH, data={
    'description': 'example',
})
```
Use encryption:
```python
ipam = PhpIpamClient(
    url='https://ipam',
    app_id='myapp',
    token='mytoken',
    encryption=True,
)
```

### Other API clients
- https://github.com/adzhurinskij/phpipam-api-pythonclient (only Python 2.7)
- https://github.com/efenian/phpipamsdk
- https://github.com/michaelluich/phpIPAM
