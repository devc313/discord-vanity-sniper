import time
import requests

DESIRED_VANITY_URL = "vanity"

LISTENER_TOKEN = "listenertokeni"

STEALER_TOKEN = "stealertokeni"

SERVER_ID = 1241231241

# saniye cinsinden denenmeden once beklenecek sure
INTERVAL = 60

def get_vanity_url(token):
    headers = {
        "Authorization": f"Bot {token}"
    }
    response = requests.get(f"https://discord.com/api/v9/guilds/{SERVER_ID}/vanity-url", headers=headers)
    return response.json()["code"]

def claim_vanity_url(token):
    headers = {
        "Authorization": f"Bot {token}"
    }
    data = {
        "code": DESIRED_VANITY_URL
    }
    response = requests.patch(f"https://discord.com/api/v9/guilds/{SERVER_ID}/vanity-url", headers=headers, json=data)
    return response.status_code == 200

def main():
    last_vanity_url = None
    while True:
        time.sleep(INTERVAL)
        current_vanity_url = get_vanity_url(LISTENER_TOKEN)
        if current_vanity_url != last_vanity_url:
            if current_vanity_url == DESIRED_VANITY_URL:
                print("vanity URL is already claimed.")
            else:
                print("vanity URL is available. attempting to claim.")
                if claim_vanity_url(STEALER_TOKEN):
                    print("vanity URL claimed successfully!")
                else:
                    print("failed to claim desired vanity url.")
            last_vanity_url = current_vanity_url

if __name__ == "__main__":
    main()