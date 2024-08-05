Sure! Here is the README for the Piopiy Voice Call Integration using Python:

# Piopiy Voice Call Integration

## Prerequisites

Before you start, ensure you have the following:

- <a href="https://git-scm.com/" target="_blank">git</a>
- <a href="https://www.python.org/" target="_blank">Python</a> (>= 3.6 required)
- <a href="https://pypi.org/project/pip/" target="_blank">pip</a>
- <a href="https://ngrok.com/" target="_blank">ngrok</a>

### Clone the repository

Use the **git clone** command to clone the PIOPIY Python example from our <a href="https://github.com/telecmi/piopiy_python_example" target="_blank">TeleCMI GitHub repository</a>.

```bash
git clone https://github.com/telecmi/piopiy_python_example.git
```

First, clone this repository to your local machine:

```sh
cd piopiy_python_example
```

### Install the required packages

Once inside the project directory, create a virtual environment and install the required packages:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Piopiy call types

This example provides detailed information on how to use the Piopiy package to manage various types of voice calls, including:


#### [Call masking](/call_masking)

- [Delivery agent to customer](/call_masking/delivery_agent_to_customer.md)

- [Customer to delivery agent](/call_masking/customer_to_delivery_agent.md)

#### [Transaction alert call](/transaction_alert_call/README.md)

#### [Order confirmation call](/order_confirmation_call/README.md)

#### [Outbound dialer](/outbound_dialer/README.md)

#### [Inbound call center](/inbound_call_center/README.md)

### Call masking

#### Delivery agent to customer

```python
from piopiy import RestClient, Action

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
```

### Transaction alert call

```python
from piopiy import RestClient, Action

def transaction_alert():
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
    transaction_alert()
```

### Order confirmation call

```python
from flask import Flask, request, jsonify
from piopiy import RestClient, Action

app = Flask(__name__)

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

### Outbound dialer

```python
from piopiy import RestClient

def outbound_dialer():
    piopiy = RestClient("your_app_id", "your_app_secret")

    customer_number = "Customer number"  # Your customer phone number with country code
    piopiy_number = "Your piopiy number"  # Your piopiy number provided by the Piopiy TeleCMI platform

    options = {
        'duration': 10,     # (Optional) Maximum duration of the call in seconds
        'timeout': 20,      # (Optional) Time to wait for the call to be answered
        'loop': 1,          # (Optional) Number of retry attempts if the call is not answered
        'ring_type': "group" # (Optional) Type of ringing for the call
    }

    try:
        # Make the call
        response = piopiy.voice.call(customer_number, piopiy_number, [], options)
        print('Success response:', response)
    except Exception as error:
        print('Error:', error)

if __name__ == '__main__':
    outbound_dialer()
```

### Inbound call center

```python
from flask import Flask, request, jsonify
from piopiy import RestClient, Action

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

### Setting Up Ngrok

To expose your local server to the internet for testing purposes, you can use ngrok.

1. Download and install ngrok from <a href="https://ngrok.com/" target="_blank">ngrok</a>.
2. Start ngrok on the port your Flask application is running:

```sh
ngrok http 3001
```

This will provide you with a public URL that you can use to test your webhook endpoints.

## Running the Examples

1. Clone the repository:

```sh
git clone https://github.com/telecmi/piopiy_python_example.git
cd piopiy_python_example
```

2. Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

4. Run the desired example script:

```sh
python app.py
```

Replace the placeholder values in the examples with your actual Piopiy credentials and phone numbers.

