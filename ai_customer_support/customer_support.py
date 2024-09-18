from flask import Flask, request, jsonify
from piopiy import Action
app = Flask(__name__)
@app.route("/python/inbound", methods=["POST"])
def inbound_call():
    action = Action()
    action.stream("WEBSOCKET_URL",{ "listen_mode":"caller", "voice_quality": "8000", "stream_on_answer": True })
    return jsonify(action.PCMO())
if __name__ == "__main__":
    app.run(port=3001, debug=True)