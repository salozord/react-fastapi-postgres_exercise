from typing import List, Optional

from pydantic import BaseModel

class OfferBase(BaseModel):
    company_name: Optional[str] = None
    location: Optional[str] = None
    salary_lower_bound: Optional[int] = None
    salary_upper_bound: Optional[int] = None
    skills: Optional[List[str]] = None

class OfferCreate(OfferBase):
    """Class to model the offer creation"""
    company_name: str
    location: str
    salary_lower_bound: int
    salary_upper_bound: int
    skills: List[str]

class OfferUpdate(OfferBase):
    """Class to model the offer update"""
    pass

# Properties shared by models stored in DB
class OfferInDBBase(OfferBase):
    id: str

    class Config:
        orm_mode = True


# Properties to return to client
class Offer(OfferInDBBase):
    pass
