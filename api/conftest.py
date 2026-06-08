import pytest
from faker import Faker

from api.client.auth_client import AuthClient
from api.client.booking_client import BookingClient
from api.models.booking import BookingCreateRequest
from api.steps.auth_steps import AuthSteps
from api.steps.booking_steps import BookingSteps
from config.config_api import Config


@pytest.fixture
def auth_client():
    return AuthClient(Config.BASE_URL)


@pytest.fixture
def booking_client():
    return BookingClient(Config.BASE_URL)


@pytest.fixture
def auth_steps(auth_client):
    return AuthSteps(auth_client)


@pytest.fixture
def booking_steps(booking_client):
    return BookingSteps(booking_client)


@pytest.fixture
def token(auth_steps):
    response = auth_steps.create_token(
        username=Config.USERNAME,
        password=Config.PASSWORD
    )

    return response.json()["token"]


@pytest.fixture
def created_booking(booking_steps):
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

    response = booking_steps.create_booking(payload)

    return response.bookingid


@pytest.fixture
def booking_payload():
    faker = Faker()

    return BookingCreateRequest(
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        totalprice=faker.random_int(min=100, max=1000),
        depositpaid=True,
        bookingdates={
            "checkin": "2026-01-01",
            "checkout": "2026-01-10"
        },
        additionalneeds="Breakfast"
    )
