from fastapi import APIRouter
from services.data_loader import load_brands

router = APIRouter()

@router.get("/")
def list_brands(q: str | None = None):
    brands = load_brands()
    if q:
        q = q.lower()
        brands = [b for b in brands if q in b["brand_name"].lower()]
    return brands
