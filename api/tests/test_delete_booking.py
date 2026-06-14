import allure
from jsonschema import validate

from api.schemas.booking_delete_schema import (
    delete_booking_response_schema,
)


@allure.feature("Booking")
@allure.story("Delete booking")
@allure.title("Удаление существующего бронирования")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_booking(
        booking_steps,
        created_booking,
        token
):
    response = booking_steps.delete_booking(
        booking_id=created_booking,
        token=token
    )

    validate(
        instance=response.text,
        schema=delete_booking_response_schema
    )


@allure.feature("Booking")
@allure.story("Delete booking")
@allure.title("Удаленное бронирование недоступно для получения")
@allure.severity(allure.severity_level.CRITICAL)
def test_deleted_booking_cannot_be_retrieved(
        booking_steps,
        created_booking,
        token
):
    booking_steps.delete_booking(
        booking_id=created_booking,
        token=token
    )

    get_response = booking_steps.get_booking_raw(created_booking, expected_status=404)

    assert get_response.status_code == 404


@allure.feature("Booking")
@allure.story("Delete booking")
@allure.title("Удаление бронирования без токена авторизации")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_booking_without_token(
        booking_steps,
        created_booking
):
    response = booking_steps.delete_booking_raw(
        booking_id=created_booking,
        token=None,
        expected_status=403
    )

    assert response.status_code == 403


@allure.feature("Booking")
@allure.story("Delete booking")
@allure.title("Удаление бронирования с невалидным токеном")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_booking_with_invalid_token(
        booking_steps,
        created_booking
):
    response = booking_steps.delete_booking_raw(
        booking_id=created_booking,
        token="invalid_token",
        expected_status=403
    )

    assert response.status_code == 403
