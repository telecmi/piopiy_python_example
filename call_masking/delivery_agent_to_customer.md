# Piopiy Voice Call Example ( Delivery Agent to Customer )

This example shows how to make a call from a delivery agent to a customer using a call masking number with the Piopiy package.

## Steps to run the code

### 1.Prerequisites

Before you start, ensure you have completed the [ prerequisite steps ](/README.md).

### 2.Configure the call parameters

Replace the value in the [ Delivery agent to customer ](/call_masking/delivery_agent_to_customer.py) code with your actual values for

- [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_python_example/blob/development/call_masking/delivery_agent_to_customer.py#L5)
- [**delivery_agent_number**](https://github.com/telecmi/piopiy_python_example/blob/development/call_masking/delivery_agent_to_customer.py#L7)
- [**call_masking_number**](https://github.com/telecmi/piopiy_python_example/blob/development/call_masking/delivery_agent_to_customer.py#L8)
- [**customer_number**](https://github.com/telecmi/piopiy_python_example/blob/development/call_masking/delivery_agent_to_customer.py#L9)

### 3.Run the code

Execute the code using Python:

```bash
python call_masking/delivery_agent_to_customer.py
```

### 4.Expected call flow

When the code is executed, the call will follow these steps:

**1.Initial call to Delivery agent:** The call is initiated to the delivery agent's number first.

**2.Delivery agent answers call:** Once the agent answers the call, the call will automatically connect to the customer's number.

You can handle these steps programmatically using the Piopiy package. Ensure that your [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_python_example/blob/development/call_masking/delivery_agent_to_customer.py#L5) are correctly configured, and the [**delivery_agent_number**](https://github.com/telecmi/piopiy_python_example/blob/development/call_masking/delivery_agent_to_customer.py#L7), [**call_masking_number**](https://github.com/telecmi/piopiy_python_example/blob/development/call_masking/delivery_agent_to_customer.py#L8), and [**customer_number**](https://github.com/telecmi/piopiy_python_example/blob/development/call_masking/delivery_agent_to_customer.py#L9) provided are valid.

## Example usage

Replace the placeholders in the code with your actual values:

```python
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

```

## Parameters type and description

These are the list of parameters and its description

#### Main parameters

| parameter             | Type   | Description                                                                   |
| --------------------- | ------ | ----------------------------------------------------------------------------- |
| app_id                | number | Your app Id provided by Piopiy TeleCMI platform.                              |
| app_secret            | string | Your app secret provided by Piopiy TeleCMI platform.                          |
| delivery_agent_number | number | The phone number of the agent receiving the call, including the country code. |
| call_masking_number   | number | The call masking number provided by the Piopiy TeleCMI platform.              |
| customer_number       | number | The phone number of the customer being called, including the country code.    |
| options               | object | An object containing optional parameters (duration, timeout & loop).          |

#### Options parameters

| parameter | Type   | Description                                                                |
| --------- | ------ | -------------------------------------------------------------------------- |
| duration  | number | The maximum duration of the call in seconds,By default 5400 seconds.       |
| timeout   | number | Time to wait for the call to be answered in seconds,By default 40 seconds. |
| loop      | number | The number of retry attempts if the call is not answered,By default 1.     |

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
