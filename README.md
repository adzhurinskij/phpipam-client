# phpipam-client
[![PyPI](https://img.shields.io/pypi/v/phpipam-client.svg)](https://pypi.org/project/phpipam-client/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/phpipam-client.svg)](https://pypi.org/project/phpipam-client/) [![Pyup Status](https://pyup.io/repos/github/adzhurinskij/phpipam-client/shield.svg)](https://pyup.io/repos/github/adzhurinskij/phpipam-client/) [![Travis (.org)](https://img.shields.io/travis/adzhurinskij/phpipam-client.svg)](https://travis-ci.org/adzhurinskij/phpipam-client)

PHPIPAM Python RESP API Client. It supports Python 2.7 and 3.4+.

### Installation
```
pip install phpipam-client
```

### Example
Basic usage:
```python
from phpipam_client import PhpIpamClient, GET, PATCH

ipam = PhpIpamClient(
    url='https://ipam',
    app_id='myapp',
    username='mylogin',
    password='mypassword',
    user_agent='myapiclient', # custom user-agent header
)

# read object
ipam.get('/sections/')

ipam.get('/sections/', {
    'filter_by': 'id',
    'filter_value': 2,
})

# create object
ipam.post('/sections/', {
    'description': 'example',
})

# update object
ipam.patch('/sections/1/', {
    'description': 'example',
})

# delete object
ipam.delete('/sections/1/')

# read object
ipam.query('/sections/', method=GET)

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
