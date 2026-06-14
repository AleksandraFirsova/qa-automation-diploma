import allure

from api.models.booking import (
    BookingCreateRequest,
    BookingCreateResponse,
    BookingModel
)


class BookingSteps:

    def __init__(self, booking_client):
        self.booking_client = booking_client

    def _assert_status(self, response, expected=200):
        assert response.status_code == expected

    @allure.step("Создать бронирование (raw)")
    def create_booking_raw(self, payload: dict, expected_status=200):
        response = self.booking_client.create_booking(payload)
        self._assert_status(response, expected=expected_status)
        return response

    @allure.step("Создать бронирование")
    def create_booking(self, payload: BookingCreateRequest) -> BookingCreateResponse:
        response = self.booking_client.create_booking(payload.model_dump())
        self._assert_status(response, expected=200)
        return BookingCreateResponse.model_validate(response.json())

    @allure.step("Получить бронирование по id={booking_id}")
    def get_booking(self, booking_id: int) -> BookingModel:
        response = self.booking_client.get_booking(booking_id)
        self._assert_status(response, expected=200)
        return BookingModel.model_validate(response.json())

    @allure.step("Получить бронирование (raw)")
    def get_booking_raw(self, booking_id: int, expected_status=200):
        response = self.booking_client.get_booking(booking_id)
        self._assert_status(response, expected=expected_status)
        return response

    @allure.step("Получить список бронирований")
    def get_booking_ids(self, params=None):
        response = self.booking_client.get_booking_ids(params=params)
        self._assert_status(response, expected=200)
        return response.json()

    @allure.step("Удалить бронирование")
    def delete_booking(self, booking_id: int, token: str):
        response = self.booking_client.delete_booking(
            booking_id=booking_id,
            token=token
        )
        self._assert_status(response, expected=201)
        return response

    @allure.step("Удалить бронирование (raw)")
    def delete_booking_raw(
            self,
            booking_id: int,
            token: str | None,
            expected_status: int
    ):
        response = self.booking_client.delete_booking(
            booking_id=booking_id,
            token=token
        )
        self._assert_status(response, expected=expected_status)
        return response

    @allure.step("Полное обновление бронирования")
    def update_booking(self, booking_id: int, payload: BookingCreateRequest, token: str) -> BookingModel:
        response = self.booking_client.update_booking(
            booking_id=booking_id,
            body=payload.model_dump(),
            token=token
        )
        self._assert_status(response, expected=200)
        return BookingModel.model_validate(response.json())

    @allure.step("Частичное обновление бронирования")
    def patch_booking(self, booking_id: int, payload: dict, token: str) -> BookingModel:
        response = self.booking_client.patch_booking(
            booking_id=booking_id,
            body=payload,
            token=token
        )
        self._assert_status(response, expected=200)
        return BookingModel.model_validate(response.json())

    @allure.step("Частичное обновление (raw)")
    def patch_booking_raw(
            self,
            booking_id: int,
            payload: dict,
            token: str | None = None,
            expected_status: int = 200
    ):
        response = self.booking_client.patch_booking(
            booking_id=booking_id,
            body=payload,
            token=token
        )
        self._assert_status(response, expected=expected_status)
        return response

    @allure.step("Создать стандартное бронирование")
    def create_default_booking(self):
        payload = BookingCreateRequest(
            firstname="Jim",
            lastname="Brown",
            totalprice=111,
            depositpaid=True,
            bookingdates={
                "checkin": "2026-01-01",
                "checkout": "2026-01-10"
            },
            additionalneeds="Breakfast"
        )
        return self.create_booking(payload)
