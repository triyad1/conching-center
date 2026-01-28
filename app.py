from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/payment", methods=["POST"])
def payment():
    data = request.json
    return jsonify({
        "status": "success",
        "message": "Payment received",
        "data": data
    })

app.run(port=5000)
