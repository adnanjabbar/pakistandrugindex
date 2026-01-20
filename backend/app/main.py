from fastapi import FastAPI
from routers import generics, brands, alternatives

app = FastAPI(
    title="Pakistan Drug Index API",
    description="Search medicines, brands, alternatives & manufacturers",
    version="1.0.0"
)

app.include_router(generics.router, prefix="/generics", tags=["Generics"])
app.include_router(brands.router, prefix="/brands", tags=["Brands"])
app.include_router(alternatives.router, prefix="/alternatives", tags=["Alternatives"])
