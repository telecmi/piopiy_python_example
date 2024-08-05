# Piopiy Voice Call Example (Customer to Delivery Agent)

This example shows how to make a call from a customer to a delivery agent using a call masking number with Piopiy package.

## Steps to run the code

### 1.Prerequisites

Before you start, ensure you have completed the [ prerequisite steps ](/README.md).

### 2.Configure the call parameters

Replace the value in the [ Customer to delivery agent ](/call_masking/customer_to_delivery_agent.py) code with your actual values for

- [**delivery_agent_number**](https://github.com/telecmi/piopiy_python_example/blob/development/call_masking/customer_to_delivery_agent.py#L10)
- [**call_masking_number**](https://github.com/telecmi/piopiy_python_example/blob/development/call_masking/customer_to_delivery_agent.py#L11)

### 3.Create and run the Flask server

Create a simple Flask server to handle inbound calls:

```python
from flask import Flask, request, jsonify
from piopiy import Action

app = Flask(__name__)

@app.route('/inbound', methods=['POST'])
def inbound():
    action = Action()

    delivery_agent_number = "Your delivery agent phone number"  # Your delivery agent phone number with country code
    call_masking_number = "Your call masking number"  # Your call masking number provided by the Piopiy TeleCMI platform

    options = {
        'duration': 10,     # (Optional) Maximum duration of the call in seconds
        'timeout': 20,      # (Optional) Time to wait for the call to be answered
        'loop': 1           # (Optional) Number of retry attempts if the call is not answered
    }

    action.call(delivery_agent_number, call_masking_number, options)
    return jsonify(action.PCMO())

if __name__ == '__main__':
    app.run(port=3001, debug=True)

```

Run the server:

```bash
python call_masking/customer_to_delivery_agent.py
```

## Parameters type and description

These are the list of parameters and its description

#### Main parameters

| parameter             | Type   | Description                                                                   |
| --------------------- | ------ | ----------------------------------------------------------------------------- |
| delivery_agent_number | number | The phone number of the agent receiving the call, including the country code. |
| call_masking_number   | number | The call masking number provided by the Piopiy TeleCMI platform.              |
| options               | object | An object containing optional parameters (duration, timeout & loop).          |

#### Options parameters

| parameter | Type   | Description                                                                |
| --------- | ------ | -------------------------------------------------------------------------- |
| duration  | number | The maximum duration of the call in seconds,By default 5400 seconds.       |
| timeout   | number | Time to wait for the call to be answered in seconds,By default 40 seconds. |
| loop      | number | The number of retry attempts if the call is not answered,By default 1.     |

### 4.Create a public URL using ngrok

To expose your local server to the internet, use ngrok to create a public URL:

```sh
ngrok http 3001
```

Copy the URL provided by ngrok. This URL will look something like **https://customer.to.delivey.agent.ngrok.io**.

### 5.Configure Piopiy dashboard

Log in to your <a href="https://developer.telecmi.com" target="_blank">Piopiy dashboard</a> and paste the ngrok URL into the "Answer URL" input field. Ensure that the endpoint is set correctly to handle inbound calls.

```sh
https://customer.to.delivey.agent.ngrok.io/inbound
```

### 6.Expected Call Flow

When the code is executed, the call will follow these steps:

**1.Initial call to Call Masking Number:** The call is initiated from the customer to the call masking number.

**2.Call received by Delivery Agent:** The delivery agent receives the call via the call masking number.
