import httpx
from app.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
from app.models import TradingViewAlert
from app.utils.logger import logger
from typing import Optional
import asyncio

class TelegramError(Exception):
    """Custom exception for Telegram-related errors"""
    pass

async def send_telegram_alert(alert: TradingViewAlert, max_retries: int = 3) -> bool:
    """
    Send alert to Telegram channel with retry logic
    
    Args:
        alert: TradingViewAlert object
        max_retries: Maximum number of retry attempts
        
    Returns:
        bool: True if message was sent successfully
        
    Raises:
        TelegramError: If message couldn't be sent after retries
    """
    if not all([TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID]):
        logger.error("Telegram configuration is missing")
        raise TelegramError("Telegram configuration is missing")

    message = (
        f"🚨 Trading Alert!\n\n"
        f"Symbol: {alert.ticker}\n"
        f"Price: ${alert.price:.2f}\n"
        f"Signal: {alert.signal}\n"
        f"Time: {alert.timestamp.strftime('%Y-%m-%d %H:%M:%S UTC')}"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    for attempt in range(max_retries):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url,
                    json={
                        "chat_id": TELEGRAM_CHAT_ID,
                        "text": message,
                        "parse_mode": "HTML"
                    },
                    timeout=10.0
                )
                
                response.raise_for_status()
                logger.info(f"Successfully sent Telegram alert for {alert.ticker}")
                return True
                
        except httpx.TimeoutException:
            logger.warning(f"Telegram request timed out (attempt {attempt + 1}/{max_retries})")
            if attempt + 1 < max_retries:
                await asyncio.sleep(2 ** attempt)  # Exponential backoff
                
        except httpx.HTTPStatusError as e:
            logger.error(f"Telegram API error: {e.response.text}")
            raise TelegramError(f"Telegram API error: {e.response.text}")
            
        except Exception as e:
            logger.error(f"Error sending Telegram alert: {e}")
            if attempt + 1 < max_retries:
                await asyncio.sleep(2 ** attempt)
            else:
                raise TelegramError(f"Failed to send Telegram alert after {max_retries} attempts") 