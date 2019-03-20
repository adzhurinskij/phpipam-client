# -*- coding: utf-8 -*-

from __future__ import absolute_import

import json
import base64
import requests

from requests.auth import HTTPBasicAuth

from . import rijndael


GET = requests.get
POST = requests.post
PATCH = requests.patch
DELETE = requests.delete


class PhpIpamException(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class PhpIpamClient(object):

    def __init__(self, url, app_id, username=None, password=None, token=None, encryption=False, timeout=None, ssl_verify=True, user_agent=None):
        self._api_url = url
        self._api_appid = app_id
        self._api_username = username
        self._api_password = password
        self._api_token = token
        self._api_encryption = encryption
        self._api_timeout = timeout
        self._api_ssl_verify = ssl_verify

        self._api_headers = {
            'content-type': 'application/json',
        }

        if user_agent:
            self._api_headers['user-agent'] = user_agent

        if not self._api_encryption:
            self.login()

    def query(self, path, method=GET, data=None, auth=None):
        _params = {}
        _data = None

        if self._api_token:
            self._api_headers['token'] = self._api_token

        if self._api_encryption:
            _url = '{}/api/'.format(self._api_url)
            _enc_data = {}

            for index, value in enumerate(list(filter(None, path.split('/')))):
                if index == 0:
                    _enc_data['controller'] = value
                elif index == 1:
                    _enc_data['id'] = value
                else:
                    _enc_data['id{}'.format(index)] = value

            if data is not None:
                _enc_data.update(data)

            _params = {
                'app_id': self._api_appid,
                'enc_request': base64.b64encode(rijndael.encrypt(self._api_token, json.dumps(_enc_data)))
            }
        else:
            _url = '{}/api/{}{}'.format(self._api_url, self._api_appid, path)

            if data is not None:
                _data = json.dumps(data)

        resp = method(
            _url,
            params=_params,
            data=_data,
            headers=self._api_headers,
            auth=auth,
            verify=self._api_ssl_verify,
            timeout=self._api_timeout,
        )

        result = resp.json()

        if resp.status_code not in (200, 201):
            raise PhpIpamException(resp.text)

        if not result['success']:
            raise PhpIpamException(resp.text)

        if 'data' in result:
            return result['data']


    def login(self):
        resp = self.query('/user/',
            method=POST,
            auth=HTTPBasicAuth(self._api_username, self._api_password),
        )

        self._api_token = resp['token']

        return resp

    def token_check(self):
        try:
            return self.query('/user/')
        except:
            return self.login()

    def token_extend(self):
        return self.query('/user/')
