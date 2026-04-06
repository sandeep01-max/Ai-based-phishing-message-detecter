from flask import Flask, render_template, request

app = Flask(__name__)

# Simulated Threat Intelligence Database
threat_keywords = [
    "login", "verify", "bank", "otp", "password",
    "click", "urgent", "account", "update", "secure"
]

def analyze_message(text, sender):
    score = 0
    detected_patterns = []

    for word in threat_keywords:
        if word in text.lower():
            score += 1
            detected_patterns.append(word)

    # Risk analysis based on sender
    if sender.startswith("+91"):
        risk = "Medium Risk ⚠️"
    else:
        risk = "High Risk 🚨"

    # Message classification
    if score >= 3:
        status = "Dangerous ❌"
    elif score == 2:
        status = "Suspicious ⚠️"
    else:
        status = "Safe ✅"

    return status, detected_patterns, risk


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    risk = ""
    patterns = []
    message = ""
    sender = ""

    if request.method == "POST":
        message = request.form["message"]
        sender = request.form["sender"]

        result, patterns, risk = analyze_message(message, sender)

    return render_template(
        "index.html",
        result=result,
        risk=risk,
        patterns=patterns,
        message=message,
        sender=sender
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
