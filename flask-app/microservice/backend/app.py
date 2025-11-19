from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS
from bson import ObjectId
from config import MONGO_URI, DB_NAME, COLLECTION_NAME
import json

app = Flask(__name__)
CORS(app)

# Mongo connection
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


# Convert ObjectId to string
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)


# @app.route("/api", methods=["GET"])
# def get_api_data():
#     with open("data.json") as f:
#         data = json.load(f)
#     return jsonify(data)


@app.route("/api", methods=["GET"])
def get_data():
    data = list(collection.find())

    # Convert each document's _id to string
    for item in data:
        item["_id"] = str(item["_id"])

    return jsonify(data)


@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = request.json
        result = collection.insert_one(data)
        return jsonify({"status": "success", "id": str(result.inserted_id)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


if __name__ == "__main__":
    app.json_encoder = JSONEncoder
    app.run(port=5000, debug=True)
