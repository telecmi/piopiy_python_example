from piopiy import RestClient

def make_call():
    # Initialize RestClient with your API Key and Secret
    piopiy = RestClient("your_app_id", "your_app_secret")

    delivery_agent_number = "Your delivery agent phone number"  # Your delivery agent phone number with country code
    call_masking_number = "Your call masking number"  # Your call masking number provided by the Piopiy TeleCMI platform
    customer_number = "Your customer number"  # Your customer phone number with country code

    options = {
        'duration': 10,     # (Optional) Maximum duration of the call in seconds
        'timeout': 20,      # (Optional) Time to wait for the call to be answered
        'loop': 1           # (Optional) Number of retry attempts if the call is not answered
    }

    try:
        # Make the call
        response = piopiy.voice.call(delivery_agent_number, call_masking_number, customer_number, options)
        print("Call connected, answer URL:", response)
    except Exception as error:
        print("Error:", error)

if __name__ == '__main__':
    make_call()
