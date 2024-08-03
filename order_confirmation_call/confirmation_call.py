from flask import Flask, request, jsonify
from piopiy import RestClient, Action

app = Flask(__name__)

# Initialize RestClient with your API Key and Secret
piopiy = RestClient("your_app_id", "your_app_secret")
action = Action()

music_file = 'Your order confimation music file or music file URL'  # Your order confimation music file or music file URL
ngrok_url = 'http://ngrok.order.confirmation.io/dtmf'  # Add your local ngrok URL
customer_number = "Your customer number"  # Your customer phone number with country code
piopiy_number = "Your piopiy number"  # Your piopiy number provided by the Piopiy TeleCMI platform
order_confimation_pcmo_function = action.PCMO()  # Use this PCMO function to confirm your order input

options = {
    'max_digit': 1,     # (Optional) Maximum number of digits expected from the user input
    'max_retry': 1,     # (Optional) Maximum number of retry attempts
    'timeout': 1        # (Optional) Time allowed between DTMF inputs in seconds
}

# Initiate the call
action.playGetInput(ngrok_url, music_file, options)

try:
    response = piopiy.voice.call(customer_number, piopiy_number, order_confimation_pcmo_function)
    print('Success response:', response)
except Exception as error:
    print('Error:', error)

# Set up the webhook server
@app.route('/dtmf', methods=['POST'])
def dtmf():
    action = Action()
    dtmf = request.json.get('dtmf')  # Assuming DTMF input is in the body of the request

    if dtmf == 1:
        action.playMusic("Your example order confirmation music file or music file URL")
        return jsonify(action.PCMO())
    else:
        action.playMusic("Your example order cancellation music file or music file URL")
        return jsonify(action.PCMO())

if __name__ == '__main__':
    app.run(port=3001, debug=True)
