import json
import os
import requests
from datetime import datetime, timedelta, timezone

# Load facts
with open("facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)

# Calculate index based on days since epoch to rotate through 300 entries
days = (datetime.now(timezone.utc) - datetime(1970,1,1, tzinfo=timezone.utc)).days
index = days % len(facts)
fact = facts[index]

# Build message
today = datetime.now(timezone.utc).astimezone().strftime("%d %b %Y")
message = f"Now it's daily time for \"Do you know?\" Fact of the Day ({today})\n\n{fact}"

# Send to Telegram
BOT_TOKEN = os.environ['TG_BOT_TOKEN']
CHAT_ID   = os.environ['TG_CHAT_ID']
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = { 'chat_id': CHAT_ID, 'text': message }

resp = requests.post(url, json=payload)
print(f"Posted fact #{index+1}: {resp.status_code}")
