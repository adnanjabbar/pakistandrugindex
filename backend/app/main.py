from fastapi import FastAPI
from routers import drugs

app = FastAPI(title="Pakistan Drug Index API")
app.include_router(drugs.router)
