from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from repositories.offer_repository import offer_repository
from core.database import get_connection
from schemas.offer import Offer, OfferCreate, OfferUpdate

router = APIRouter(
    prefix="/offers",
    tags=["offers"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Offer])
async def get_offers(
    db: Session = Depends(get_connection),
    skip: int = 0,
    limit: int = 25
) -> Any:
    """Retrieves the list of offers based on a certain filters"""
    return offer_repository.get_multi_with_filters(db, skip=skip, limit=limit)


@router.get("/{offer_id}", response_model=Offer)
async def get_offer(offer_id: str, db: Session = Depends(get_connection)) -> Any:
    offer = offer_repository.get(db, id=offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer


@router.post("/", response_model=Offer)
async def create_offer(
    *,
    db: Session = Depends(get_connection),
    offer_in: OfferCreate
) -> Any:
    """Creates a new offer"""
    offer = offer_repository.create(db, obj_in=offer_in)
    return offer

@router.put("/{offer_id}", response_model=Offer)
async def update_offer(
    *,
    db: Session = Depends(get_connection),
    offer_id: str,
    offer_in: OfferUpdate
) -> Any:
    """Updates an existing offer"""
    offer = offer_repository.get(db, id=offer_id)
    if not offer:
        raise HTTPException(
            status_code=404,
            detail="Offer does not exist",
        )
    offer = offer_repository.update(db, db_obj=offer, obj_in=offer_in)
    return offer


@router.delete("/{offer_id}", response_model=Offer)
async def delete_offer(offer_id: str, db: Session = Depends(get_connection)) -> Any:
    """Removes an offer from the DB"""
    offer = offer_repository.remove(db, id=offer_id)
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer
