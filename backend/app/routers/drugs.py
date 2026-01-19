from fastapi import APIRouter
import json, os

router = APIRouter(prefix="/drugs", tags=["Drugs"])

DATA_DIR = "backend/app/data"

@router.get("/")
def list_drugs():
    drugs = []
    for f in os.listdir(DATA_DIR):
        with open(os.path.join(DATA_DIR, f)) as fh:
            drugs.append(json.load(fh))
    return drugs
