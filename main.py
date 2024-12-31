from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    auth = request.headers.get("Authorization")
    if (auth != key):
        return jsonify({"error": "Unauthorized"}), 401
    else:
        data = request.json  
        print(f"Received data: {data}")
        return jsonify({"status": "success", "received": data}), 200
        



if __name__ == "__main__":
    f = open('secretkey.txt')
    key = f.read()
    app.run(host="0.0.0.0", port=5000)

