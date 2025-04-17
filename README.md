# TradingView Alert System

A FastAPI-based system that receives TradingView alerts via webhook and forwards them to various notification channels (Telegram, Email, Discord).

## Features

- Webhook endpoint for TradingView alerts
- Real-time Telegram notifications
- Structured alert data validation
- Extensible notification system
- Error handling and logging

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your credentials:
   ```bash
   cp .env.example .env
   ```
4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

Once running, visit:
- http://localhost:8000/docs - Swagger UI
- http://localhost:8000/redoc - ReDoc UI

## TradingView Alert Setup

1. In TradingView, create a new alert
2. Set webhook URL to: `http://your-domain/webhook`
3. Use the following JSON payload format:
   ```json
   {
     "ticker": "{{ticker}}",
     "price": {{close}},
     "signal": "{{strategy.order.action}}",
     "timestamp": "{{time}}"
   }
   ```

## Environment Variables

Required environment variables:
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `TELEGRAM_CHAT_ID`: Your Telegram chat ID

Optional:
- `DISCORD_WEBHOOK_URL`: Discord webhook URL
- `EMAIL_SMTP_USER`: Email username
- `EMAIL_SMTP_PASS`: Email password
- `DATABASE_URL`: Database connection string

## Development

To run tests:
```bash
pytest
```

## License

MIT 