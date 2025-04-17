from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TradingViewAlert(BaseModel):
    ticker: str
    price: float
    signal: str
    timestamp: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "ticker": "SPY",
                "price": 412.38,
                "signal": "rsi_oversold",
                "timestamp": "2025-04-17T12:32:00Z"
            }
        }

class NotificationResponse(BaseModel):
    status: str
    message: str
    timestamp: datetime = datetime.now()
    error: Optional[str] = None 