from pydantic import BaseModel, Field


class PhishingScanRequest(BaseModel):
    text: str = Field(..., min_length=10, examples=["Urgent: verify your bank account now at http://fake-bank.com"])
    channel: str = Field(default="email", examples=["email", "sms"])
