from api.client.base_client import BaseClient


class AuthClient(BaseClient):
    AUTH = "/auth"

    def create_token(self, username: str, password: str):
        body = {
            "username": username,
            "password": password
        }

        headers = {
            "Content-Type": "application/json"
        }

        return self.send_request(
            method="POST",
            url=self.AUTH,
            json=body,
            headers=headers
        )

    def create_token_with_empty_body(self):
        headers = {
            "Content-Type": "application/json"
        }

        return self.send_request(
            method="POST",
            url=self.AUTH,
            json={},
            headers=headers
        )
