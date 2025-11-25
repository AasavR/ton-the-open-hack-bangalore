import hmac
import hashlib
import time
from fastapi import HTTPException

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'  # To be set from env variables

def verify_telegram_auth(auth_data: dict) -> dict:
    """
    Verifies Telegram WebApp authentication data using the bot token.
    Throws HTTPException if verification fails.
    Returns verified user data on success.
    """

    # Extract hash and data fields
    received_hash = auth_data.get('hash')
    if not received_hash:
        raise HTTPException(status_code=400, detail="Missing hash in auth data")

    # Check timestamp to prevent replay attacks
    auth_date = int(auth_data.get('auth_date', 0))
    if time.time() - auth_date > 86400:
        raise HTTPException(status_code=403, detail="Auth data is too old")

    # Prepare data check string
    data_check_arr = []
    for key, value in sorted(auth_data.items()):
        if key != 'hash':
            data_check_arr.append(f"{key}={value}")
    data_check_string = "\n".join(data_check_arr)

    # Calculate secret key from bot token
    secret_key = hashlib.sha256(TELEGRAM_BOT_TOKEN.encode()).digest()

    # Calculate HMAC-SHA256 of the data_check_string using secret key
    hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    if hmac_hash != received_hash:
        raise HTTPException(status_code=403, detail="Invalid Telegram auth data")

    # Verification successful; return relevant user data
    user_info = {
        "id": auth_data.get("id"),
        "first_name": auth_data.get("first_name"),
        "last_name": auth_data.get("last_name"),
        "username": auth_data.get("username"),
        "photo_url": auth_data.get("photo_url"),
    }
    return user_info
