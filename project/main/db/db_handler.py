from pydantic import BaseModel

class BTC(BaseModel):
    base: str
    currency: str
    amount: float