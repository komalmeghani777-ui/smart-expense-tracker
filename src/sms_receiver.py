# src/sms_receiver.py

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms():
    data = request.json
    message = data.get("message", "")

    # Detect amount (Rs / ₹ / INR + number)
    match = re.search(r'(?:rs\.?|₹|inr)\s*([0-9]+(?:\.[0-9]{1,2})?)', message.lower())

    if match:
        amount = float(match.group(1))
        # Save temporarily so Streamlit can show it
        with open("pending_sms.txt", "w") as f:
            f.write(str(amount))
        return jsonify({"status": "detected", "amount": amount})

    return jsonify({"status": "no_amount_found"})


if __name__ == "__main__":
    app.run(port=8000)
