import json as json_lib

import allure
import requests


class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(
            self,
            method,
            url,
            json=None,
            headers=None,
            params=None,
            data=None
    ):
        full_url = self.base_url + url

        response = requests.request(
            method=method,
            url=full_url,
            json=json,
            headers=headers,
            params=params,
            data=data
        )

        allure.attach(
            f"{method} {full_url}",
            name="Request URL",
            attachment_type=allure.attachment_type.TEXT
        )

        if json is not None:
            allure.attach(
                json_lib.dumps(json, indent=2, ensure_ascii=False),
                name="Request Body",
                attachment_type=allure.attachment_type.JSON
            )

        allure.attach(
            str(response.status_code),
            name="Status Code",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            response.text,
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )

        return response
