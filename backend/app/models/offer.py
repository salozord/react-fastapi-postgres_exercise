from sqlalchemy import Column, Integer, String, ARRAY

from core.database import Base

class Offer(Base):
    __tablename__ = "offers"

    id = Column(String, server_default="gen_random_uuid()", primary_key=True, index=True)
    company_name = Column(String, index=True, nullable=False)
    location = Column(String, index=True, nullable=False)
    salary_lower_bound = Column(Integer, index=True, nullable=False)
    salary_upper_bound = Column(Integer, index=True, nullable=False)
    skills = Column(ARRAY(String), index=True, nullable=False)