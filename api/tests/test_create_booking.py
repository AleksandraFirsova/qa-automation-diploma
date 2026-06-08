import allure
import pytest
from faker import Faker
from jsonschema import validate

from api.models.booking import BookingCreateRequest
from api.schemas.booking_create_response_schema import (
    booking_create_response_schema,
)

faker = Faker()


@allure.feature("Booking")
@allure.story("Create booking")
@allure.title("Проверка структуры ответа при создании бронирования")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_booking(booking_steps):
    payload = BookingCreateRequest(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        totalprice=111,
        depositpaid=True,
        bookingdates={
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        additionalneeds="Breakfast"
    ).model_dump()

    response = booking_steps.create_booking_raw(payload)

    validate(
        instance=response.json(),
        schema=booking_create_response_schema
    )


@allure.feature("Booking")
@allure.story("Create booking")
@allure.title("Созданное бронирование содержит переданные данные")
def test_create_booking_returns_sent_data(booking_steps):
    payload = BookingCreateRequest(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        totalprice=999,
        depositpaid=False,
        bookingdates={
            "checkin": "2026-01-01",
            "checkout": "2026-01-10"
        },
        additionalneeds="Dinner"
    )

    response_model = booking_steps.create_booking(payload)

    assert response_model.booking.firstname == payload.firstname
    assert response_model.booking.lastname == payload.lastname
    assert response_model.booking.totalprice == payload.totalprice
    assert response_model.booking.depositpaid == payload.depositpaid
    assert response_model.booking.additionalneeds == payload.additionalneeds


@allure.feature("Booking")
@allure.story("Create booking")
@allure.title("Каждое новое бронирование получает уникальный идентификатор")
def test_create_booking_generates_unique_ids(booking_steps):
    payload = BookingCreateRequest(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        totalprice=111,
        depositpaid=True,
        bookingdates={
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        additionalneeds="Breakfast"
    )

    first_response = booking_steps.create_booking(payload)
    second_response = booking_steps.create_booking(payload)

    assert first_response.bookingid != second_response.bookingid


@allure.feature("Booking")
@allure.story("Create booking")
@allure.title("Созданное бронирование доступно по полученному идентификатору")
@allure.severity(allure.severity_level.CRITICAL)
def test_created_booking_can_be_retrieved(booking_steps):
    payload = BookingCreateRequest(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        totalprice=500,
        depositpaid=True,
        bookingdates={
            "checkin": "2026-06-01",
            "checkout": "2026-06-05"
        },
        additionalneeds="Breakfast"
    )

    create_response = booking_steps.create_booking(payload)
    booking_id = create_response.bookingid

    booking_model = booking_steps.get_booking(booking_id)

    assert booking_model.firstname == payload.firstname
    assert booking_model.lastname == payload.lastname
    assert booking_model.totalprice == payload.totalprice
    assert booking_model.depositpaid == payload.depositpaid
    assert booking_model.additionalneeds == payload.additionalneeds


@allure.feature("Booking")
@allure.story("Create booking")
@allure.title("Ответ содержит корректный booking id")
def test_create_booking_returns_booking_id(booking_steps):
    payload = BookingCreateRequest(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        totalprice=111,
        depositpaid=True,
        bookingdates={
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        additionalneeds="Breakfast"
    )

    response_model = booking_steps.create_booking(payload)

    assert isinstance(response_model.bookingid, int)
    assert response_model.bookingid > 0


@allure.feature("Booking")
@allure.story("Create booking")
@allure.title("Создание бронирования с различным статусом депозита")
@pytest.mark.parametrize("deposit_paid", [True, False])
def test_create_booking_with_different_deposit_status(
        booking_steps,
        deposit_paid
):
    payload = BookingCreateRequest(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        totalprice=111,
        depositpaid=deposit_paid,
        bookingdates={
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        additionalneeds="Breakfast"
    )

    response_model = booking_steps.create_booking(payload)

    assert response_model.booking.depositpaid == deposit_paid


@allure.feature("Booking")
@allure.story("Create booking")
@allure.title("Невозможно создать бронирование без обязательного поля firstname")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_booking_without_firstname(booking_steps):
    payload = {
        "lastname": faker.last_name(),
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = booking_steps.create_booking_raw(payload, expected_status=500)

    assert response.status_code != 200, "API должен отклонять невалидный запрос"
