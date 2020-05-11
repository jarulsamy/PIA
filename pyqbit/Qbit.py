import json

import requests
from requests import HTTPError


class Qbit(object):
    def __init__(self, host, user, password):
        if host[-1] == "/":
            host = host[:-1]

        self.host = host
        self.api_endpoint = f"{self.host}/api/v2"
        self.headers = {"Referer": self.host}

        self.user = user
        self.password = password
        self.sess = requests.session()

        self._login()

    def _login(self):

        login_payload = {"username": self.user, "password": self.password}

        resp = self.sess.post(
            f"{self.api_endpoint}/auth/login", headers=self.headers, data=login_payload
        )

        if resp.status_code != 200:
            raise HTTPError(f"Erroneous HTTP response: {resp.status_code}")

    def _logout(self):
        self.sess.post(f"{self.api_endpoint}auth/logout")

    def get_api_version(self):
        resp = self.sess.get(f"{self.api_endpoint}/app/webapiVersion")
        return resp.json()

    def get_preferences(self):
        resp = self.sess.get(f"{self.api_endpoint}/app/preferences")
        return resp.json()

    def set_preference(self, payload):
        payload = f"json={json.dumps(payload)}"
        headers = {"content-type": "application/x-www-form-urlencoded"}
        resp = self.sess.post(
            f"{self.api_endpoint}/app/setPreferences", data=payload, headers=headers
        )
