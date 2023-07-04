from typing import List

from sqlalchemy.orm import Session

from .base_repository import BaseRepository
from models.offer import Offer
from schemas.offer import OfferCreate, OfferUpdate


class OfferRepository(BaseRepository[Offer, OfferCreate, OfferUpdate]):
    """Repository for the Offer class which accesses the database table"""
    def get_multi_with_filters(
        self, db: Session, *, skip: int = 0, limit: int = 25
    ) -> List[Offer]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )


offer_repository = OfferRepository(Offer)