from flask import Flask, request, jsonify
from piopiy import Action

app = Flask(__name__)

@app.route('/inbound-call', methods=['POST'])
def inbound_call():
    action = Action()

    multiple_agent_number = ["Your agent phone number", "Your agent phone number"]  # Multiple agent's phone numbers with country code
    piopiy_number = "Your piopiy number"  # Your piopiy number provided by the Piopiy TeleCMI platform

    options = {
        'duration': 10,     # (Optional) Maximum duration of the call in seconds
        'timeout': 20,      # (Optional) Time to wait for the call to be answered
        'loop': 1,          # (Optional) Number of retry attempts if the call is not answered
        'ring_type': "group" # (Optional) Type of ringing for the call
    }

    action.call(multiple_agent_number, piopiy_number, options)
    return jsonify(action.PCMO())

if __name__ == '__main__':
    app.run(port=3001, debug=True)
