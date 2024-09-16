from flask import Flask, request, jsonify
from piopiy import Action

app = Flask(__name__)

@app.route('/basic', methods=['POST'])
def inbound_call():
    action = Action()

    # Define your numbers
    agent_number = "Your agent phone number"  # Your agent phone number with country code.
    piopiy_number = "Your piopiy number"      # Your Piopiy number provided by the Piopiy TeleCMI platform.

    # Options for the call
    options = {
        'duration': 10,     # (Optional) Maximum duration of the call in seconds
        'timeout': 20,      # (Optional) Time to wait for the call to be answered
        'loop': 1           # (Optional) Number of retry attempts if the call is not answered
    }

    # Make the call to the agent
    response = action.call(agent_number, piopiy_number, options)

    # Return the response from the action
    return jsonify({'status': 'call initiated', 'response': response})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
