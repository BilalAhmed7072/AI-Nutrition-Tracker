from flask import Flask, jsonify
from routes.upload_routes import upload_bp
from routes.assistant_route import assistant_bp

app = Flask(__name__)
app.register_blueprint(upload_bp, url_prefix="/api")
app.register_blueprint(assistant_bp, url_prefix="/api")

@app.route('/')
def home():
    return jsonify({"status": "Nutrition Tracker AI Backend running"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
