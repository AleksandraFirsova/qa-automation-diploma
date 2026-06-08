from api.client.base_client import BaseClient


class BookingClient(BaseClient):
    BOOKING = "/booking"

    def get_booking_ids(self, params=None):
        return self.send_request(
            method="GET",
            url=self.BOOKING,
            params=params
        )

    def get_booking(self, booking_id: int, headers=None):
        return self.send_request(
            method="GET",
            url=f"{self.BOOKING}/{booking_id}",
            headers=headers
        )

    def create_booking(self, body):
        return self.send_request(
            method="POST",
            url=self.BOOKING,
            json=body,
            headers={"Content-Type": "application/json"})

    def update_booking(self, booking_id: int, body: dict, token: str):
        return self.send_request(
            method="PUT",
            url=f"{self.BOOKING}/{booking_id}",
            json=body,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Cookie": f"token={token}"
            }
        )

    def patch_booking(
            self,
            booking_id: int,
            body: dict,
            token: str
    ):
        return self.send_request(
            method="PATCH",
            url=f"{self.BOOKING}/{booking_id}",
            json=body,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Cookie": f"token={token}"
            }
        )

    def delete_booking(
            self,
            booking_id: int,
            token: str
    ):
        return self.send_request(
            method="DELETE",
            url=f"{self.BOOKING}/{booking_id}",
            headers={
                "Cookie": f"token={token}"
            }
        )
