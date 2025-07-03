from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# Load MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["todo_db"]
todos = db["todos"]

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    item_name = request.form.get("itemName")
    item_desc = request.form.get("itemDescription")
    todos.insert_one({"name": item_name, "description": item_desc})
    return jsonify({"message": "Data submitted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
