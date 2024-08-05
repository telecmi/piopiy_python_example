# Piopiy Voice Call Example (Inbound Call Center)

This example shows how to set up an inbound call center using the Piopiy package.

## Steps to run the code

### 1.Prerequisites

Before you start, ensure you have completed the [ prerequisite steps ](/README.md).

### 2.Configure the call parameters

Replace the value in the [ Inbound call center ](/inbound_call_center/inbound_call.py) code with your actual values for

- [**multiple_agent_number**](https://github.com/telecmi/piopiy_python_example/blob/development/inbound_call_center/inbound_call.py#L10)

- [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/inbound_call_center/inbound_call.py#L11)

### 3.Create and run the Flask server

Create a simple Flask server to handle inbound calls:

```python
from flask import Flask, request, jsonify
from piopiy import Action

app = Flask(__name__)

@app.route('/inbound-call', methods=['POST'])
def inbound_call():
    action = Action()

    multiple_agent_number = ["Your agent phone number", "Your agent phone number"]  # Multiple agent's phone numbers with country code
    piopiy_number = "Your piopiy number"  # Your piopiy number provided by the Piopiy TeleCMI platform

    options = {
        'duration': 10,     # (Optional) Maximum duration of the call in seconds
        'timeout': 20,      # (Optional) Time to wait for the call to be answered
        'loop': 1,          # (Optional) Number of retry attempts if the call is not answered
        'ring_type': "group" # (Optional) Type of ringing for the call
    }

    action.call(multiple_agent_number, piopiy_number, options)
    return jsonify(action.PCMO())

if __name__ == '__main__':
    app.run(port=3001, debug=True)

```

Run the server:

```bash
python inbound_call_center/inbound_call.py
```

## Parameters type and description

These are the list of parameters and its description

#### Main parameters

| parameter             | Type   | Description                                                             |
| --------------------- | ------ | ----------------------------------------------------------------------- |
| piopiy_number         | number | The piopiy number provided by the Piopiy TeleCMI platform.              |
| multiple_agent_number | array  | An array of phone numbers for multiple agents, including country codes. |
| options               | object | An object containing optional parameters (duration, timeout & loop).    |

#### Options parameters

| parameter | Type   | Description                                                                |
| --------- | ------ | -------------------------------------------------------------------------- |
| duration  | number | The maximum duration of the call in seconds,By default 5400 seconds.       |
| timeout   | number | Time to wait for the call to be answered in seconds,By default 40 seconds. |
| loop      | number | The number of retry attempts if the call is not answered,By default 1.     |
| ring_type | string | The type of ringing for the call. By default, it is **single**, where agents receive calls one by one. If set to **group**, all agents will receive calls simultaneously.                          |

### 4.Create a public URL using ngrok

To expose your local server to the internet, use ngrok to create a public URL:

```sh
ngrok http 3001
```

Copy the URL provided by ngrok. This URL will look something like **https://inbound.call.center.ngrok.io**.

### 5.Configure Piopiy dashboard

Log in to your <a href="https://developer.telecmi.com" target="_blank">Piopiy dashboard</a> and paste the ngrok URL into the "Answer URL" input field. Ensure that the endpoint is set correctly to handle inbound calls.

```sh
https://inbound.call.center.ngrok.io/inbound-call
```

### 6.Expected Call Flow

When the code is executed, the call will follow these steps:

**1.Customer Calls Piopiy Number:** The customer initiates the call to the Piopiy number.

**2.Call is Routed to Agents:** The call is routed to the agents' numbers provided in the multiple_agent_number array.

You can handle these steps programmatically using the Piopiy package. Ensure that your [multiple_agent_number](https://github.com/telecmi/piopiy_python_example/blob/development/inbound_call_center/inbound_call.py#L10) and [piopiy_number](https://github.com/telecmi/piopiy_python_example/blob/development/inbound_call_center/inbound_call.py#L11) are correctly configured.
