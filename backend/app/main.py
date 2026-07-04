from fastapi import FastAPI
from app.routers import categories, transactions, budgets, analytics

app = FastAPI(title="SpendWise API")

app.include_router(categories.router)
app.include_router(transactions.router)
app.include_router(budgets.router)
app.include_router(analytics.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
