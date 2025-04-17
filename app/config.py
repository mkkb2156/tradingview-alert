from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# API Configuration
API_VERSION = "1.0.0"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Notification Services
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
EMAIL_SMTP_USER = os.getenv("EMAIL_SMTP_USER")
EMAIL_SMTP_PASS = os.getenv("EMAIL_SMTP_PASS")

# Optional: Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL") 