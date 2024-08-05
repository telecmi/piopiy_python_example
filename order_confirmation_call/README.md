# Piopiy Voice Call Example ( Order Confirmation Call )

This example shows how to make an order confirmation call using the Piopiy package.

## Steps to run the code

### 1.Prerequisites

Before you start, ensure you have completed the [ prerequisite steps ](/README.md).

### 2.Configure the call parameters

Replace the value in the [ order confirmation call ](/order_confirmation_call/confirmation_call.py) code with your actual values for

- [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L7)
- [**ngrok URL**](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L11)
- [**music_file**](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L10)
- [**customer_number**](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L12)
- [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L13)

### 3. Create a public URL using ngrok

To expose your local server to the internet, use ngrok to create a public URL:

```sh
ngrok http 3001
```

Copy the URL provided by ngrok. This URL will look something like **https://ngrok.order.confirmation.io**.

### 4.Configure piopiy to use the ngrok URL

In your code where you configure the [ngrok URL](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L11), replace it with the copied Ngrok URL, appending the **/dtmf** path. For example:

```bash
const ngrok_url = 'https://ngrok.order.confirmation.io/dtmf';  # Replace with your actual Ngrok URL
```

This URL is used to send requests to your local server, specifically to the **/dtmf** endpoint that handles DTMF inputs.

### 5.Run the code

Execute the code using Python:

```bash
python order_confirmation_call/confirmation_call.py
```

### 6. Expected call flow

When the code is executed, the call will follow these steps:

**1.Initial Call to Customer:** The call is initiated to the customer's number first.

**2.Customer Answers Call:** Once the customer answers the call, a prompt for order confimation music plays.

**3.DTMF Handling:** TThe customer presses 1 to confirm the order or presses any other input to cancel the order.

**4.Response Handling:**

- If the customer presses 1, a confirmation music file plays, indicating the order was confirmed.
- If the customer does not press 1 or presses another input, an order cancellation music file plays, indicating the order was canceled.

You can handle these steps programmatically using the Piopiy package. Ensure that your [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L7) are correctly configured, and the [**music_file**](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L10), [**customer_number**](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L12), [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L13) and [**ngrok URL**](https://github.com/telecmi/piopiy_python_example/blob/development/order_confirmation_call/confirmation_call.py#L11) provided are valid.

## Example usage

Replace the placeholders in the code with your actual values:

```python
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

```

## Parameters type and description

These are the list of parameters and its description

#### Main parameters

| parameter       | Type   | Description                                                                        |
| --------------- | ------ | ---------------------------------------------------------------------------------- |
| app_id          | number | Your app Id provided by Piopiy TeleCMI platform.                                   |
| app_secret      | string | Your app secret provided by Piopiy TeleCMI platform.                               |
| music_file      | string | The music file or music file URL of the order confimation music file to be played. |
| customer_number | number | The phone number of the customer receiving the call, including the country code.   |
| piopiy_number   | number | The piopiy number provided by the Piopiy TeleCMI platform.                         |
| options         | object | An object containing optional parameters (max_digit, max_retry & timeout).         |

#### Options parameters

| parameter | Type   | Description                                                             |
| --------- | ------ | ----------------------------------------------------------------------- |
| max_digit | number | Maximum number of digits expected from the user input.                  |
| max_retry | number | Maximum number of retry attempts.                                       |
| timeout   | number | Time allowed between DTMF inputs in seconds.By default, it is 1 second. |

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
