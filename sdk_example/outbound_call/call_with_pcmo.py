from piopiy import RestClient, Action

def main():
    # Initialize the RestClient with your appid and app token
    piopiy = RestClient("your_appid", "your_app_token")

    # Define PCMO actions
    action = Action()

    try:
        customer_number = "Your customer number"  # Your customer phone number with country code.
        piopiy_number = "Your piopiy number"      # Your piopiy number provided by the Piopiy TeleCMI platform.
        agent_number = "Your agent phone number"   # Your agent phone number with country code.

        # PCMO actions to execute during the call
        pcmo_function = action.PCMO()

        # Options for the call
        options = {
            'duration': 10,   # (Optional) Maximum duration of the call in seconds
            'timeout': 20,    # (Optional) Time to wait for the call to be answered
            'loop': 1,        # (Optional) Number of retry attempts if the call is not answered
            'record': True    # (Optional) Whether to record the call
        }

        # Play music before the call
        action.playMusic('https://example.com/your_music_file.wav')

        # Initiate the call to the customer
        action.call(agent_number, piopiy_number, options)

        # Make the call to the agent with PCMO actions
        response = piopiy.voice.call(customer_number, piopiy_number, pcmo_function, options)

        print('Call with PCMO actions connected, answer URL:', response)

    except Exception as error:
        print('Error:', error)

if __name__ == '__main__':
    main()
