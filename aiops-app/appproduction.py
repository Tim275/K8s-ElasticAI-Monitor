from flask import Flask, request, jsonify
import logging
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import json

app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

MODEL_API_URL = "http://3.122.232.116:11434/api/chat"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1322372258173554850/ZSvXe3V3SOvnc_Ixc3jd8fH5U55_IC7pzKbtmgVCtPGONJoxu_enBmbZ0mp9WJYrvYqU"

session = requests.Session()
retries = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[408, 429, 500, 502, 503, 504]
)
session.mount('http://', HTTPAdapter(max_retries=retries))

@app.route('/alert', methods=['POST'])
def receive_alert():
    try:
        # Log raw request data for debugging
        app.logger.info(f"Request headers: {request.headers}")
        raw_data = request.get_data(as_text=True)
        app.logger.info(f"Request data: {raw_data}")
        
        try:
            alert_data = request.get_json()
            if not alert_data:
                return jsonify({"status": "error", "message": "Empty payload"}), 400
        except Exception as e:
            app.logger.error(f"JSON parsing error: {e}")
            return jsonify({"status": "error", "message": "Invalid JSON payload"}), 400
        
        app.logger.info(f"Parsed alert payload: {alert_data}")

        # Handle list payload directly since it's coming as array from Elasticsearch
        alert_message = {
            "model": "mistral-nemo",
            "messages": [
                {
                    "role": "user",
                    "content": f"As a DevOps Engineer analyzing logs from k8s-infra*, provide brief analysis and solutions (max 1500 chars): {alert_data}"
                }
            ],
            "stream": False
        }

        # Send to AI model
        model_response = session.post(
            MODEL_API_URL,
            headers={"Content-Type": "application/json"},
            json=alert_message,
            timeout=180
        )

        if model_response.status_code != 200:
            app.logger.error(f"Model API error: {model_response.text}")
            return jsonify({"status": "error", "message": "Model analysis failed"}), 500

        # Process AI response
        analysis_content = model_response.json().get("message", {}).get("content", "No analysis")
        truncated_content = analysis_content[:1500] + ("..." if len(analysis_content) > 1500 else "")
        app.logger.info(f"Analysis received: {truncated_content[:200]}...")

        # Discord message with static index info since it's coming from watcher config
        discord_message = {
            "content": f"🚨 **Log Analysis Alert**\n📊 *Source Index: k8s-infra**\n\n{truncated_content}\n\n⚠️ *Check logs in k8s-infra**"
        }

        if len(discord_message["content"]) > 1900:
            discord_message["content"] = discord_message["content"][:1897] + "..."

        discord_response = session.post(
            DISCORD_WEBHOOK_URL,
            headers={"Content-Type": "application/json"},
            json=discord_message,
            timeout=30
        )

        if discord_response.status_code != 204:
            app.logger.error(f"Discord error: {discord_response.text}")
            return jsonify({"status": "error", "message": "Discord notification failed"}), 500

        return jsonify({"status": "success", "message": "Alert processed"}), 200

    except requests.Timeout:
        app.logger.error("Request timed out")
        return jsonify({"status": "error", "message": "Timeout"}), 504
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.logger.info("Starting AIOps Service on port 5000...")
    app.run(host='0.0.0.0', port=5000)