from flask import Flask, request, jsonify
from piopiy import Action

app = Flask(__name__)

@app.route('/pcmo', methods=['POST'])
def inbound_call():

    action = Action()

    agent_number = "Your agent phone number"  # Your agent phone number with country code.
    
    piopiy_number = "Your piopiy number"  # Your piopiy number provided by the Piopiy TeleCMI platform

    options = {
        'duration': 10,     # (Optional) Maximum duration of the call in seconds
        'timeout': 20,      # (Optional) Time to wait for the call to be answered
        'loop': 1           # (Optional) Number of retry attempts if the call is not answered
    }

    # Play a music file during the call
    action.playMusic('https://example.com/your_music_file.wav')

    # Initiate the call to the agent's number
    action.call(agent_number, piopiy_number, options)

    # Return the response in JSON format
    return jsonify(action.PCMO())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
