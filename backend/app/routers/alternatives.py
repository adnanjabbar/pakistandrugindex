from fastapi import APIRouter
from services.data_loader import load_brands
from services.alternative_engine import find_alternatives

router = APIRouter()

@router.get("/{brand_id}")
def alternatives(brand_id: str):
    brands = load_brands()
    return find_alternatives(brands, brand_id)
