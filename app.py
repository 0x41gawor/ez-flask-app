from flask import Flask, jsonify
import os
from pymongo import MongoClient
app = Flask(__name__)

def get_db():
    conn = MongoClient('mongodb://ejek:ejek@localhost:27017/')
    db = conn['ez_flask_app_db']
    return db

@app.route("/")
def hello():
    db = get_db()
    _animals = db.ez_flask_app_db.find()
    
    animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
    return jsonify({"animals": animals})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)