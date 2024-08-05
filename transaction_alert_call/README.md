# Piopiy Voice Call Example ( Transaction Alert Call )

This example shows how to make a transaction alert call using the Piopiy package.

## Steps to run the code

### 1.Prerequisites

Before you start, ensure you have completed the [ prerequisite steps ](/README.md).

### 2.Configure the call parameters

Replace the value in the [ Transaction alert call ](/transaction_alert_call/alert_call.py) code with your actual values for

- [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_python_example/blob/development/transaction_alert_call/alert_call.py#L5)
- [**music_file**](https://github.com/telecmi/piopiy_python_example/blob/development/transaction_alert_call/alert_call.py#L8)
- [**customer_number**](https://github.com/telecmi/piopiy_python_example/blob/development/transaction_alert_call/alert_call.py#L9)
- [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/transaction_alert_call/alert_call.py#L10)

### 3.Run the code

Execute the code using Python:

```bash
python transaction_alert_call/alert_call.py
```

### 4.Expected call flow

When the code is executed, the call will follow these steps:

**1.Initial Call to Customer:** The call is initiated to the customer's number first.

**2.Customer Answers Call:** Once the customer answers the call, alert music is played to notify them of the transaction.

You can handle these steps programmatically using the Piopiy package. Ensure that your [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_python_example/blob/development/transaction_alert_call/alert_call.py#L5) are correctly configured, and the [**music_file**](https://github.com/telecmi/piopiy_python_example/blob/development/transaction_alert_call/alert_call.py#L8), [**customer_number**](https://github.com/telecmi/piopiy_python_example/blob/development/transaction_alert_call/alert_call.py#L9) and [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/transaction_alert_call/alert_call.py#L10) provided are valid.

## Example usage

Replace the placeholders in the code with your actual values:

```python
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
```

## Parameters type and description

These are the list of parameters and its description

| parameter       | Type   | Description                                                                      |
| --------------- | ------ | -------------------------------------------------------------------------------- |
| app_id          | number | Your app Id provided by Piopiy TeleCMI platform.                                 |
| app_secret      | string | Your app secret provided by Piopiy TeleCMI platform.                             |
| music_file      | string | The music file or music file URL of the alert music file to be played.           |
| customer_number | number | The phone number of the customer receiving the call, including the country code. |
| piopiy_number   | number | The piopiy number provided by the Piopiy TeleCMI platform.                       |

## Sample response

Below is the following sample call response.

```python

{
  "data": { "status": 'progress' },
  "status": 'progress',
  "request_id": 'X0uoi5LT5vCMOG6CZGEdMMYD5RL9raaEFa1p1IQ9EVm',
  "cmi_code": 200
}

```

## Properties

These are the list of properties and its description

| Property   | Type   | Description                  |
| ---------- | ------ | ---------------------------- |
| status     | string | The Status of the call.      |
| request_id | string | The Unique ID for this call. |

## HTTP status codes

| cmi_code | cmi_code type | Description              |
| -------- | ------------- | ------------------------ |
| 200      | Success       | We received the request. |
| 401      | Error         | Authentication failed.   |
