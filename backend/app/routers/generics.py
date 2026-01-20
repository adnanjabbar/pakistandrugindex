from fastapi import APIRouter
from services.data_loader import load_brands

router = APIRouter()

@router.get("/")
def list_generics():
    brands = load_brands()
    return sorted(list(set(b["generic_id"] for b in brands)))
