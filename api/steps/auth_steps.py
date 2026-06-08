import allure


class AuthSteps:

    def __init__(self, auth_client):
        self.auth_client = auth_client

    @allure.step("Создать токен для пользователя '{username}'")
    def create_token(self, username: str, password: str):
        return self.auth_client.create_token(
            username=username,
            password=password
        )

    @allure.step("Создать токен с пустым телом запроса")
    def create_token_with_empty_body(self):
        return self.auth_client.create_token_with_empty_body()
