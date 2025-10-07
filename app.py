from flask import Flask, jsonify, request
import json
from ai_module import analyze_feedback

app = Flask(__name__)
DB_FILE = "inventory.json"

# Initialize DB
def init_db():
    try:
        with open(DB_FILE, "r") as f:
            json.load(f)
    except:
        with open(DB_FILE, "w") as f:
            json.dump([], f)

init_db()

@app.route("/")
def home():
    return {"message": "Smart Inventory API is running!"}

@app.route("/inventory", methods=["GET"])
def get_inventory():
    with open(DB_FILE, "r") as f:
        return jsonify(json.load(f))

@app.route("/add", methods=["POST"])
def add_item():
    item = request.get_json()
    with open(DB_FILE, "r") as f:
        data = json.load(f)
    data.append(item)  # ? Add the new item to inventory
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
    return jsonify({"success": True, "message": "Item added!"})

@app.route("/feedback",methods=["POST"])

def feedback():
    data=request.get_json()
    feedback_text=data.get("feedback","")
    sentiment=analyze_feedback(feedback_text)
    return jsonify({"feedback":feedback_text,"sentiment_score":sentiment})

if __name__ == "__main__":
    app.run(debug=True)
