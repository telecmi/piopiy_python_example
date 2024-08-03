# Piopiy Voice Call Example ( Outbound Dialer )

This example shows how to make an outbound dialer using the Piopiy package.

## Steps to run the code

### 1.Prerequisites

Before you start, ensure you have completed the [ prerequisite steps ](/README.md).

### 2.Configure the call parameters

Replace the value in the [ Outbound Dialer ](/outbound_dialer/dialer_call.js) code with your actual values for

- [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_node_example/blob/development/outbound_dialer/dialer_call.js#L2)
- [**customer_number**](https://github.com/telecmi/piopiy_node_example/blob/development/outbound_dialer/dialer_call.js#L4)
- [**piopiy_number**](https://github.com/telecmi/piopiy_node_example/blob/development/outbound_dialer/dialer_call.js#L5)
- [**multiple_agent_number**](https://github.com/telecmi/piopiy_node_example/blob/development/outbound_dialer/dialer_call.js#L6)

### 3.Run the code

Execute the code using Node.js:

```sh
node outbound_dialer/dialer_call.js
```

### 4.Expected call flow

When the code is executed, the call will follow these steps:

**1.Initial Call to Customer:** The call is initiated to the customer's number first.

**2.Customer Answers Call:** Once the customer answers the call, the call is routed to one of the agent numbers.

You can handle these steps programmatically using the Piopiy package. Ensure that your [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_node_example/blob/development/outbound_dialer/dialer_call.js#L2), [**customer_number**](https://github.com/telecmi/piopiy_node_example/blob/development/outbound_dialer/dialer_call.js#L4), [**piopiy_number**](https://github.com/telecmi/piopiy_node_example/blob/development/outbound_dialer/dialer_call.js#L5), and [**multiple_agent_number**](https://github.com/telecmi/piopiy_node_example/blob/development/outbound_dialer/dialer_call.js#L6) provided are valid.

## Example usage

Replace the placeholders in the code with your actual values:

```javascript
const { Piopiy } = require("piopiy");
const piopiy = new Piopiy("your_app_id", "your_app_secret");

const customer_number = "Your customer number"; // Your customer phone number with country code.
const piopiy_number = "Your piopiy number"; // Your piopiy number provided by the Piopiy TeleCMI platform.
const multiple_agent_number = ["Your agent phone number", "Your agent phone number"]; // Multiple agent's phone number with country code.
const options = {
  duration: 10, // (Optional) Maximum duration of the call in seconds.
  timeout: 20, // (Optional) Time to wait for the call to be answered.
  loop: 1, // (Optional) Number of retry attempts if the call is not answered.
  ring_type: "group", // (Optional) Type of ringing for the call.
};

piopiy.voice.call(customer_number, piopiy_number, multiple_agent_number, options)
  .then((res) => {
    console.log("Success res:", res);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
```

## Parameters type and description

These are the list of parameters and its description

#### Main Parameters

| parameter             | Type   | Description                                                                     |
| --------------------- | ------ | ------------------------------------------------------------------------------- |
| app_id                | number | Your app Id provided by Piopiy TeleCMI platform.                                |
| app_secret            | string | Your app secret provided by Piopiy TeleCMI platform.                            |
| customer_number       | number | The phone number of the customer being called, including the country code.      |
| piopiy_number         | number | The piopiy number provided by the Piopiy TeleCMI platform.                      |
| multiple_agent_number | array  | An array of phone numbers for multiple agents, including country codes.         |
| options               | object | An object containing optional parameters (duration, timeout, loop & ring_type). |

#### Options Parameters

| parameter | Type   | Description                                                                |
| --------- | ------ | -------------------------------------------------------------------------- |
| duration  | number | The maximum duration of the call in seconds,By default 5400 seconds.       |
| timeout   | number | Time to wait for the call to be answered in seconds,By default 40 seconds. |
| loop      | number | The number of retry attempts if the call is not answered,By default 1.     |
| ring_type | string | The type of ringing for the call. By default, it is **single**, where agents receive calls one by one. If set to **group**, all agents will receive calls simultaneously.                          |

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
