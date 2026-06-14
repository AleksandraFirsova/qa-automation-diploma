import allure

from api.models.booking import BookingCreateRequest


@allure.feature("Booking")
@allure.story("Update booking")
@allure.title("Полное обновление существующего бронирования")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_booking(
        booking_steps,
        created_booking,
        token
):
    payload = BookingCreateRequest(
        firstname="James",
        lastname="Brown",
        totalprice=222,
        depositpaid=False,
        bookingdates={
            "checkin": "2026-01-01",
            "checkout": "2026-01-10"
        },
        additionalneeds="Dinner"
    )

    response = booking_steps.update_booking(
        booking_id=created_booking,
        payload=payload,
        token=token
    )

    assert response.firstname == payload.firstname
    assert response.lastname == payload.lastname
    assert response.totalprice == payload.totalprice
    assert response.depositpaid == payload.depositpaid
    assert response.additionalneeds == payload.additionalneeds

    assert response.bookingdates.checkin == payload.bookingdates.checkin
    assert response.bookingdates.checkout == payload.bookingdates.checkout


@allure.feature("Booking")
@allure.story("Partial update booking")
@allure.title("Частичное обновление имени гостя")
@allure.severity(allure.severity_level.CRITICAL)
def test_patch_booking_firstname(
        booking_steps,
        created_booking,
        token
):
    response = booking_steps.patch_booking(
        booking_id=created_booking,
        payload={"firstname": "James"},
        token=token
    )

    assert response.firstname == "James"


@allure.feature("Booking")
@allure.story("Partial update booking")
@allure.title("Частичное обновление изменяет только указанные поля")
def test_patch_booking_updates_only_specified_fields(
        booking_steps,
        created_booking,
        token
):
    original = booking_steps.get_booking(created_booking)

    response = booking_steps.patch_booking(
        booking_id=created_booking,
        payload={"firstname": "Updated"},
        token=token
    )

    assert response.firstname == "Updated"

    assert response.lastname == original.lastname
    assert response.totalprice == original.totalprice
    assert response.depositpaid == original.depositpaid


@allure.feature("Booking")
@allure.story("Partial update booking")
@allure.title("Частичное обновление нескольких полей")
def test_patch_booking_multiple_fields(
        booking_steps,
        created_booking,
        token
):
    response = booking_steps.patch_booking(
        booking_id=created_booking,
        payload={
            "firstname": "Alex",
            "lastname": "Firsova"
        },
        token=token
    )

    assert response.firstname == "Alex"
    assert response.lastname == "Firsova"


@allure.feature("Booking")
@allure.story("Partial update booking")
@allure.title("Частичное обновление без токена авторизации")
@allure.severity(allure.severity_level.NORMAL)
def test_patch_booking_without_token(
        booking_steps,
        created_booking
):
    response = booking_steps.patch_booking_raw(
        booking_id=created_booking,
        payload={"firstname": "James"},
        expected_status=403
    )

    assert response.status_code == 403


@allure.feature("Booking")
@allure.story("Partial update booking")
@allure.title("Частичное обновление с невалидным токеном")
@allure.severity(allure.severity_level.NORMAL)
def test_patch_booking_with_invalid_token(
        booking_steps,
        created_booking
):
    response = booking_steps.patch_booking_raw(
        booking_id=created_booking,
        payload={"firstname": "James"},
        token="invalid_token",
        expected_status=403
    )

    assert response.status_code == 403
