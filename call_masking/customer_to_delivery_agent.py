from flask import Flask, request, jsonify
from piopiy import Action

app = Flask(__name__)

@app.route('/inbound', methods=['POST'])
def inbound():
    action = Action()

    delivery_agent_number = "Your delivery agent phone number"  # Your delivery agent phone number with country code
    call_masking_number = "Your call masking number"  # Your call masking number provided by the Piopiy TeleCMI platform

    options = {
        'duration': 10,     # (Optional) Maximum duration of the call in seconds
        'timeout': 20,      # (Optional) Time to wait for the call to be answered
        'loop': 1           # (Optional) Number of retry attempts if the call is not answered
    }

    action.call(delivery_agent_number, call_masking_number, options)
    return jsonify(action.PCMO())

if __name__ == '__main__':
    app.run(port=3001, debug=True)
