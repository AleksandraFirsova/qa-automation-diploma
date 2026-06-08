from pydantic import BaseModel


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingCreateRequest(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None = None


class BookingPatchRequest(BaseModel):
    firstname: str | None = None
    lastname: str | None = None
    totalprice: int | None = None
    depositpaid: bool | None = None
    additionalneeds: str | None = None


class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None = None


class BookingCreateResponse(BaseModel):
    bookingid: int
    booking: BookingModel
