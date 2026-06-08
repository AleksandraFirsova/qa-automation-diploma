import requests


class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, method, url, json=None, headers=None, params=None, data=None):
        full_url = self.base_url + url
        print(f"{method} {full_url}")

        return requests.request(
            method=method,
            url=full_url,
            json=json,
            headers=headers,
            params=params,
            data=data
        )
