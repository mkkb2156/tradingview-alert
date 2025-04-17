from fastapi import APIRouter, HTTPException, Request
from app.models import TradingViewAlert, NotificationResponse
from app.services.telegram import send_telegram_alert
from app.utils.logger import logger
from datetime import datetime
import json

router = APIRouter()

@router.post("/webhook", response_model=NotificationResponse)
async def receive_alert(request: Request):
    try:
        # Log incoming request
        body = await request.body()
        logger.info(f"Received webhook request: {body.decode()}")
        
        # Parse and validate alert data
        try:
            data = await request.json()
            alert = TradingViewAlert(**data)
            logger.info(f"Validated alert data for {alert.ticker}")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON payload: {e}")
            raise HTTPException(status_code=400, detail="Invalid JSON payload")
        except Exception as e:
            logger.error(f"Validation error: {e}")
            raise HTTPException(status_code=422, detail=str(e))

        # Send alert to Telegram
        await send_telegram_alert(alert)
        logger.info(f"Successfully sent alert for {alert.ticker} to Telegram")
        
        return NotificationResponse(
            status="success",
            message="Alert processed and sent successfully",
            timestamp=datetime.now()
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing alert: {e}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        ) 