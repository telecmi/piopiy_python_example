from piopiy import RestClient

def main():
    # Initialize the RestClient with your appid and app token
    piopiy = RestClient("your_appid", "your_app_token")

    try:
        # Define multiple agent numbers
        multiple_agent_numbers = ["Your agent phone number", "Your agent phone number"]  # Multiple agent's phone numbers with country codes.
        piopiy_number = "Your piopiy number"  # Your Piopiy number provided by the Piopiy TeleCMI platform.
        customer_number = "Your customer number"  # Your customer phone number with country code.

        # Options for the call
        options = {
            "duration": 10,  # (Optional) Maximum duration of the call in seconds
            "timeout": 20,   # (Optional) Time to wait for the call to be answered
            "loop": 1,       # (Optional) Number of retry attempts if the call is not answered
            "record": True   # (Optional) Whether to record the call
        }

        # Make the call to the multiple agents
        response = piopiy.voice.call(customer_number, piopiy_number, multiple_agent_numbers, options)

        print('Call to multiple numbers connected, answer URL:', response)

    except Exception as error:
        print('Error:', error)

if __name__ == '__main__':
    main()
