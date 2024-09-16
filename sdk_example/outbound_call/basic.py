from piopiy import RestClient

def main():
    # Initialize the RestClient with your appid and app token
    piopiy = RestClient("your_appid", "your_app_token")

    try:
        agent_number = "Your agent phone number"  # Your agent phone number with country code.
        piopiy_number = "Your piopiy number"      # Your Piopiy number provided by the Piopiy TeleCMI platform.
        customer_number = "Your customer number"   # Your customer phone number with country code.

        # Options for the call
        options = {
            "duration": 10,  # (Optional) Maximum duration of the call in seconds
            "timeout": 20,   # (Optional) Time to wait for the call to be answered
            "loop": 1,       # (Optional) Number of retry attempts if the call is not answered
            "record": True   # (Optional) Whether to record the call
        }

        # Make the call
        response = piopiy.voice.call(agent_number, piopiy_number, customer_number, options)

        print('Call connected, answer URL:', response)

    except Exception as error:
        print('Error:', error)

if __name__ == '__main__':
    main()
    