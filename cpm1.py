import requests
import json
import getpass
import time
from datetime import datetime

# --- Game Service Configuration ---
FIREBASE_API_KEY = 'AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM'
FIREBASE_LOGIN_URL = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={FIREBASE_API_KEY}"
RANK_URL = "https://us-central1-cp-multiplayer.cloudfunctions.net/SetUserRating4"

# --- Multiple accounts list (SAFE) ---
ACCOUNTS = [
    {"email": "kingcpmcpm1@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm2@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm3@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm4@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm5@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm6@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm7@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm8@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm9@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm10@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm11@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm12@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm13@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm14@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm15@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm16@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm17@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm19@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm20@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm21@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm22@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm23@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm24@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm25@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm26@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm27@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm28@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm29@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm30@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm31@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm32@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm33@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm34@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm35@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm36@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm37@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm39@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm40@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm41@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm42@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm43@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm44@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm45@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm46@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm47@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm48@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm49@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm50@gmail.com", "password": "666666"},
    {"email": "kingcpmcpm51@gmail.com", "password": "666666"},
]
def login(email, password):
    """Login to CPM using Firebase API."""
    print(f"\n🔐 Logging in as {email}...")
    payload = {
        "clientType": "CLIENT_TYPE_ANDROID",
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    headers = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12)",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(FIREBASE_LOGIN_URL, headers=headers, json=payload)
        response_data = response.json()

        if response.status_code == 200 and 'idToken' in response_data:
            print("✅ Login successful!")
            return response_data.get('idToken')
        else:
            error_message = response_data.get("error", {}).get("message", "Unknown error during login.")
            print(f"❌ Login failed: {error_message}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return None


def set_rank(token):
    """Set KING RANK using max rating data."""
    print("👑 Applying rank...")
    rating_data = {k: 100000 for k in [
        "cars", "car_fix", "car_collided", "car_exchange", "car_trade", "car_wash",
        "slicer_cut", "drift_max", "drift", "cargo", "delivery", "taxi", "levels", "gifts",
        "fuel", "offroad", "speed_banner", "reactions", "police", "run", "real_estate",
        "t_distance", "treasure", "block_post", "push_ups", "burnt_tire", "passanger_distance"
    ]}
    rating_data["time"] = 10000000000
    rating_data["race_win"] = 3000

    payload = {"data": json.dumps({"RatingData": rating_data})}
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "okhttp/3.12.13"
    }

    try:
        response = requests.post(RANK_URL, headers=headers, json=payload)
        if response.status_code == 200:
            print("✅ Rank request sent.")
            return True
        else:
            print(f"❌ Failed. HTTP Status: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False


def main_logic():
    """Automatic processing of multiple accounts."""
    print("\nKing Rank Script (SAFE MODE, MULTI ACCOUNT ENABLED)")

    for acc in ACCOUNTS:
        email = acc["email"]
        password = acc["password"]

        print(f"\n➡️ Processing account: {email}")

        auth_token = login(email, password)
        if auth_token:
            if set_rank(auth_token):
                print("✅ Finished for this account.")
            else:
                print("❌ Rank failed.")
        else:
            print("❌ Login failed for this account.")


if __name__ == "__main__":
    main_logic()
