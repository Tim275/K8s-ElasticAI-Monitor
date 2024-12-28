from flask import Flask, request, jsonify
import logging
import requests
import json

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Configuration for model API and Discord webhook
MODEL_API_URL = "http://18.191.107.234:11434/api/chat"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1322372258173554850/ZSvXe3V3SOvnc_Ixc3jd8fH5U55_IC7pzKbtmgVCtPGONJoxu_enBmbZ0mp9WJYrvYqU"


@app.route('/alert', methods=['POST'])
def receive_alert():
    try:
        # Get the JSON payload from the request
        alert_data = request.get_json()
        
        # Log the received alert data for debugging purposes
        app.logger.info(f"Received alert: {alert_data}")

        # Prepare the alert message for the model
        alert_message = {
            "model": "mistral-nemo",
            "messages": [
                {
                    "role": "user",
                    "content": f"You are a Senior DevOps Engineer and you are receiving a TOP 20 count from a ElasticSearch index, that one alert send wh reach over some thresold. Analyze this alert message, provide possible solutions for then and return usin less than 1900 characters, because Discord limit is this. Here is the  aler data for you to analyse and provide insights and fixes: {alert_data}"
                }
            ],
            "stream": False
        }

        # Send the alert data to the Llama3 model API
        model_response = requests.post(
            MODEL_API_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(alert_message)
        )


        # Handle potential issues with model API response
        if model_response.status_code != 200:
            app.logger.error(f"Model API error: {model_response.text}")
            return jsonify({"status": "error", "message": "Failed to get analysis from model"}), 500


        # Extract the model's analysis from the response
        model_analysis = model_response.json()
        analysis_content = model_analysis.get("message", {}).get("content", "No analysis available")

        print(analysis_content)

        # Format the message for Discord
        discord_message = {
            "content": f"**Alert Analysis**:\n{analysis_content}\n** Please check your application to reduce the logs**"
        }


        # Send the analysis to the Discord webhook
        discord_response = requests.post(
            DISCORD_WEBHOOK_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(discord_message)
        )

        # Check if the Discord webhook message was sent successfully
        if discord_response.status_code != 204:
            app.logger.error(f"Discord webhook error: {discord_response.text}")
            return jsonify({"status": "error", "message": "Failed to send message to Discord"}), 500

        # Send a JSON response back to acknowledge receipt of the alert
        return jsonify({"status": "success", "message": "Alert received and processed"}), 200

    except Exception as e:
        app.logger.error(f"Error processing alert: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)