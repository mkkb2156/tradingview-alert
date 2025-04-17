from fastapi import FastAPI
from app.routes import webhook

app = FastAPI(
    title="TradingView Alert System",
    description="A system for processing TradingView alerts and sending notifications",
    version="1.0.0"
)

app.include_router(webhook.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 