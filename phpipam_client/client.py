# -*- coding: utf-8 -*-

import json
import requests

from requests.auth import HTTPBasicAuth


class PhpIpamException(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class PhpIpamClient(object):

    def __init__(self, url, app_id, username=None, password=None, token=None, timeout=None, ssl_verify=True, user_agent=None):
        self._api_url = url
        self._api_appid = app_id
        self._api_username = username
        self._api_password = password
        self._api_token = token
        self._api_timeout = timeout
        self._api_ssl_verify = ssl_verify

        self._api_url_base = '{}/api/{}'.format(
            self._api_url,
            self._api_appid,
        )

        self._api_headers = {
            'content-type': 'application/json',
        }

        if user_agent:
            self._api_headers['user-agent'] = user_agent

        self.login()

    def query(self, path, method=requests.get, data=None, auth=None):

        if self._api_token:
            self._api_headers['token'] = self._api_token

        if data is not None:
            if type(data) != str:
                data = json.dumps(data)

            if method == requests.get:
                method = requests.post

        resp = method(
            '{}{}'.format(self._api_url_base, path),
            data=data,
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

        return result['data']

    def login(self):
        resp = self.query('/user/',
            method=requests.post,
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
