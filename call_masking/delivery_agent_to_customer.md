# Piopiy Voice Call Example ( Delivery Agent to Customer )

This example shows how to make a call from a delivery agent to a customer using a call masking number with the Piopiy package.

## Steps to run the code

### 1.Prerequisites

Before you start, ensure you have completed the [ prerequisite steps ](/README.md).

### 2.Configure the call parameters

Replace the value in the [ Delivery agent to customer ](/call_masking/delivery_agent_to_customer.js) code with your actual values for

- [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_node_example/blob/development/call_masking/delivery_agent_to_customer.js#L2)
- [**delivery_agent_number**](https://github.com/telecmi/piopiy_node_example/blob/development/call_masking/delivery_agent_to_customer.js#L4)
- [**call_masking_number**](https://github.com/telecmi/piopiy_node_example/blob/development/call_masking/delivery_agent_to_customer.js#L5)
- [**customer_number**](https://github.com/telecmi/piopiy_node_example/blob/development/call_masking/delivery_agent_to_customer.js#L6)

### 3.Run the code

Execute the code using Node.js:

```sh
node call_masking/delivery_agent_to_customer.js
```

### 4.Expected call flow

When the code is executed, the call will follow these steps:

**1.Initial call to Delivery agent:** The call is initiated to the delivery agent's number first.

**2.Delivery agent answers call:** Once the agent answers the call, the call will automatically connect to the customer's number.

You can handle these steps programmatically using the Piopiy package. Ensure that your [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_node_example/blob/development/call_masking/delivery_agent_to_customer.js#L2) are correctly configured, and the [**delivery_agent_number**](https://github.com/telecmi/piopiy_node_example/blob/development/call_masking/delivery_agent_to_customer.js#L4), [**call_masking_number**](https://github.com/telecmi/piopiy_node_example/blob/development/call_masking/delivery_agent_to_customer.js#L5), and [**customer_number**](https://github.com/telecmi/piopiy_node_example/blob/development/call_masking/delivery_agent_to_customer.js#L6) provided are valid.

## Example usage

Replace the placeholders in the code with your actual values:

```javascript
const { Piopiy } = require("piopiy");
const piopiy = new Piopiy("your_app_id", "your_app_secret");

const delivery_agent_number = "Your delivery agent number"; // Example delivery agent phone number
const call_masking_number = "Your call masking number"; // Example call masking number
const customer_number = "Your customer number"; // Example customer phone number
const options = { duration: 15, timeout: 25, loop: 2 };

piopiy.voice.call(delivery_agent_number, call_masking_number, customer_number, options)
  .then((res) => {
    console.log("Sucess response:", res);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
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

```javascript

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
