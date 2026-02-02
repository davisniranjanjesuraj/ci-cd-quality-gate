from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "UP"}), 200

    @app.route("/login", methods=["POST"])
    def login():
        data = request.json
        if data.get("username") == "admin" and data.get("password") == "admin123":
            return jsonify({"message": "Login successful"}), 200
        return jsonify({"message": "Invalid credentials"}), 401

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
