import allure
from jsonschema import validate

from api.models.booking import BookingCreateRequest
from api.schemas.booking_get_schema import booking_schema


@allure.feature("Booking")
@allure.story("Get booking")
@allure.title("Получение списка идентификаторов бронирований")
def test_get_booking_ids(booking_steps):
    data = booking_steps.get_booking_ids()

    assert isinstance(data, list)
    assert len(data) > 0
    assert "bookingid" in data[0]


@allure.feature("Booking")
@allure.story("Get booking")
@allure.title("Проверка схемы ответа бронирования")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_booking_schema(booking_steps):
    payload = BookingCreateRequest(
        firstname="SchemaTest",
        lastname="User",
        totalprice=111,
        depositpaid=True,
        bookingdates={
            "checkin": "2026-01-01",
            "checkout": "2026-01-10"
        },
        additionalneeds="Breakfast"
    )

    created = booking_steps.create_booking(payload)

    response = booking_steps.get_booking_raw(
        created.bookingid,
        expected_status=200
    )

    validate(
        instance=response.json(),
        schema=booking_schema
    )


@allure.feature("Booking")
@allure.story("Get booking")
@allure.title("Получение бронирования по идентификатору")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_booking_by_id(booking_steps):
    payload = BookingCreateRequest(
        firstname="GetTest",
        lastname="User",
        totalprice=250,
        depositpaid=True,
        bookingdates={
            "checkin": "2026-01-01",
            "checkout": "2026-01-10"
        },
        additionalneeds="Breakfast"
    )

    created = booking_steps.create_booking(payload)

    booking = booking_steps.get_booking(created.bookingid)

    assert booking.firstname == payload.firstname
    assert booking.lastname == payload.lastname
    assert booking.totalprice == payload.totalprice
    assert booking.depositpaid == payload.depositpaid
    assert booking.bookingdates.checkin == payload.bookingdates.checkin
    assert booking.bookingdates.checkout == payload.bookingdates.checkout


@allure.feature("Booking")
@allure.story("Get booking")
@allure.title("Фильтрация бронирований по имени и фамилии")
def test_get_booking_filtered(booking_steps):
    payload = BookingCreateRequest(
        firstname="FilterTest",
        lastname="User",
        totalprice=111,
        depositpaid=True,
        bookingdates={
            "checkin": "2026-01-01",
            "checkout": "2026-01-10"
        },
        additionalneeds="Breakfast"
    )

    created = booking_steps.create_booking(payload)

    params = {
        "firstname": payload.firstname,
        "lastname": payload.lastname
    }

    data = booking_steps.get_booking_ids(params=params)

    assert isinstance(data, list)
    assert any(item["bookingid"] == created.bookingid for item in data)


@allure.feature("Booking")
@allure.story("Get booking")
@allure.title("Получение бронирования по несуществующему идентификатору")
@allure.severity(allure.severity_level.NORMAL)
def test_get_booking_by_invalid_id(booking_steps):
    response = booking_steps.get_booking_raw(
        999999999999,
        expected_status=404
    )

    assert response.status_code == 404


@allure.feature("Booking")
@allure.story("Get booking")
@allure.title("Повторные запросы возвращают одинаковые данные")
def test_get_booking_is_deterministic(booking_steps):
    payload = BookingCreateRequest(
        firstname="StableTest",
        lastname="User",
        totalprice=111,
        depositpaid=True,
        bookingdates={
            "checkin": "2026-01-01",
            "checkout": "2026-01-10"
        },
        additionalneeds="Breakfast"
    )

    created = booking_steps.create_booking(payload)

    first = booking_steps.get_booking(created.bookingid)
    second = booking_steps.get_booking(created.bookingid)

    assert first == second


@allure.feature("Booking")
@allure.story("Get booking")
@allure.title("Фильтрация по несуществующему имени возвращает пустой список")
@allure.severity(allure.severity_level.NORMAL)
def test_get_booking_filtered_negative(booking_steps):
    params = {
        "firstname": "NonExistingName"
    }

    data = booking_steps.get_booking_ids(params=params)

    assert data == []
