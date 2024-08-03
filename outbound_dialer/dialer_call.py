from piopiy import RestClient

def make_call():
    # Initialize RestClient with your API Key and Secret
    piopiy = RestClient("your_app_id", "your_app_secret")

    customer_number = "Customer number"  # Your customer phone number with country code
    piopiy_number = "Your piopiy number"  # Your piopiy number provided by the Piopiy TeleCMI platform
    multiple_agent_number = ["Your agent phone number", "Your agent phone number"]  # Multiple agent's phone numbers with country code

    options = {
        'duration': 10,     # (Optional) Maximum duration of the call in seconds
        'timeout': 20,      # (Optional) Time to wait for the call to be answered
        'loop': 1,          # (Optional) Number of retry attempts if the call is not answered
        'ring_type': "group" # (Optional) Type of ringing for the call
    }

    try:
        # Make the call
        response = piopiy.voice.call(customer_number, piopiy_number, multiple_agent_number, options)
        print('Success response:', response)
    except Exception as error:
        print('Error:', error)

if __name__ == '__main__':
    make_call()
