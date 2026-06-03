from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(..., examples=["admin@fraudshield.ai"])
    password: str = Field(min_length=4)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    email: str
    full_name: str
    role: str


class UserOut(BaseModel):
    id: int
    email: str
    full_name: str
    role: str

    model_config = {"from_attributes": True}
