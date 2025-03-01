from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    city = data.get("city", "")

    if not city:
        return jsonify({"error": "City is required"}), 400

    return jsonify({"message": f"Город {city} получен сервером!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
