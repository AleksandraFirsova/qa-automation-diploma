from typing import Optional

from pydantic import BaseModel


class AuthResponse(BaseModel):
    token: Optional[str] = None


class AuthErrorResponse(BaseModel):
    reason: Optional[str] = None
