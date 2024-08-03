from piopiy import RestClient, Action

def main():
    # Initialize RestClient with your API Key and Secret
    piopiy = RestClient("your_app_id", "your_app_secret")
    action = Action()

    music_file = 'Your alert music file or music file URL'  # Your alert music file or music file URL
    customer_number = "Customer number"  # Your customer phone number with country code
    piopiy_number = "Your piopiy number"  # Your piopiy number provided by the Piopiy TeleCMI platform
    alert_music_pcmo_function = action.PCMO()  # Use this PCMO function to play your alert music

    action.playMusic(music_file)

    options = {
        'duration': 10,     # (Optional) Maximum duration of the call in seconds
        'timeout': 20,      # (Optional) Time to wait for the call to be answered
        'loop': 1,          # (Optional) Number of retry attempts if the call is not answered
        'ring_type': "group" # (Optional) Type of ringing for the call
    }

    try:
        # Make the call
        response = piopiy.voice.call(customer_number, piopiy_number, alert_music_pcmo_function, options)
        print('Success response:', response)
    except Exception as error:
        print('Error:', error)

if __name__ == '__main__':
    main()
