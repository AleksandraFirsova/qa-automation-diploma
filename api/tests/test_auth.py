import allure
from jsonschema import validate

from api.models.auth import (
    AuthResponse,
    AuthErrorResponse,
)
from api.schemas.auth_schema import (
    auth_success_schema,
    auth_error_schema,
)
from config.api_config import ApiConfig


@allure.feature("Authentication")
@allure.story("Create token")
@allure.title("Успешное получение токена")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_token_success(auth_steps):
    response = auth_steps.create_token(
        username=ApiConfig.USERNAME,
        password=ApiConfig.PASSWORD
    )

    assert response.status_code == 200

    json_data = response.json()

    validate(
        instance=json_data,
        schema=auth_success_schema
    )

    data = AuthResponse.model_validate(json_data)

    assert len(data.token) > 0


@allure.feature("Authentication")
@allure.story("Create token")
@allure.title("Авторизация с неверными учетными данными")
@allure.severity(allure.severity_level.NORMAL)
def test_create_token_invalid_credentials(auth_steps):
    response = auth_steps.create_token(
        username="wrong_user",
        password="wrong_pass"
    )

    assert response.status_code == 200

    json_data = response.json()

    validate(
        instance=json_data,
        schema=auth_error_schema
    )

    data = AuthErrorResponse.model_validate(json_data)

    assert data.reason == "Bad credentials"


@allure.feature("Authentication")
@allure.story("Create token")
@allure.title("Авторизация с пустым username")
@allure.severity(allure.severity_level.NORMAL)
def test_create_token_empty_username(auth_steps):
    response = auth_steps.create_token(
        username="",
        password=ApiConfig.PASSWORD
    )

    assert response.status_code == 200

    json_data = response.json()

    validate(
        instance=json_data,
        schema=auth_error_schema
    )

    data = AuthErrorResponse.model_validate(json_data)

    assert data.reason == "Bad credentials"


@allure.feature("Authentication")
@allure.story("Create token")
@allure.title("Авторизация с пустым password")
@allure.severity(allure.severity_level.NORMAL)
def test_create_token_empty_password(auth_steps):
    response = auth_steps.create_token(
        username=ApiConfig.USERNAME,
        password=""
    )

    assert response.status_code == 200

    json_data = response.json()

    validate(
        instance=json_data,
        schema=auth_error_schema
    )

    data = AuthErrorResponse.model_validate(json_data)

    assert data.reason == "Bad credentials"


@allure.feature("Authentication")
@allure.story("Create token")
@allure.title("Авторизация с пустым телом запроса")
@allure.severity(allure.severity_level.NORMAL)
def test_create_token_empty_body(auth_steps):
    response = auth_steps.create_token_with_empty_body()

    assert response.status_code == 200

    json_data = response.json()

    validate(
        instance=json_data,
        schema=auth_error_schema
    )

    data = AuthErrorResponse.model_validate(json_data)

    assert data.reason == "Bad credentials"
