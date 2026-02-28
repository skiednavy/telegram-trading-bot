from flask import Flask, request, jsonify
import requests
import os

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

app = Flask(__name__)

def send_telegram(text: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    r = requests.post(url, json=payload)
    return r.ok

@app.get("/")
def home():
    return "Bot Running ✅"

@app.post("/webhook")
def webhook():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "Alert received")
    send_telegram(message)
    return jsonify({"status": "ok"})
