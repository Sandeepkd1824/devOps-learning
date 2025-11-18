from flask import Flask, request, render_template
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from flask import jsonify
import os

load_dotenv()
mongo_db_url = os.getenv("mongo_db_url")


# Create a new client and connect to the server
client = MongoClient(mongo_db_url)

db = client.manwal

collection = db["flask-tutorial"]

app = Flask(__name__)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


@app.route("/")
def home():
    return render_template("index.html",name="manwal")


# @app.route("/submit")
# def form_data():
#     first_name = request.args.get("first_name")
#     last_name = request.args.get("last_name")
#     email = request.args.get("email")
#     password = request.args.get("password")
#     return render_template(
#         "display_form_data.html",
#         first_name=first_name,
#         last_name=last_name,
#         email=email,
#         password=password,
#     )


@app.route("/submit", methods=["POST"])
def form_data():
    form_data = dict(request.form)

    # Insert into MongoDB
    result = collection.insert_one(form_data)

    # Convert ObjectId to string for JSON
    form_data["_id"] = str(result.inserted_id)

    return jsonify(form_data)


@app.route("/view-data")
def get_data():
    data = list(collection.find())

    # Convert each document's _id to string
    for item in data:
        item["_id"] = str(item["_id"])

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
