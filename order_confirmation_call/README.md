# Piopiy Voice Call Example ( Order Confirmation Call )

This example shows how to make an order confirmation call using the Piopiy package.

## Steps to run the code

### 1.Prerequisites

Before you start, ensure you have completed the [ prerequisite steps ](/README.md).

### 2.Configure the call parameters

Replace the value in the [ order confirmation call ](/order_confirmation_call/confirmation_call.js) code with your actual values for

- [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L6)
- [**ngrok URL**](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L10)
- [**music_file**](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L9)
- [**customer_number**](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L11)
- [**piopiy_number**](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L12)

### 3. Create a public URL using ngrok

To expose your local server to the internet, use ngrok to create a public URL:

```sh
ngrok http 3001
```

Copy the URL provided by ngrok. This URL will look something like **https://ngrok.order.confirmation.io**.

### 4.Configure piopiy to use the ngrok URL

In your code where you configure the [ngrok URL](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L10), replace it with the copied Ngrok URL, appending the **/dtmf** path. For example:

```sh
const ngrok_url = 'https://ngrok.order.confirmation.io/dtmf'; // Replace with your actual Ngrok URL
```

This URL is used to send requests to your local server, specifically to the **/dtmf** endpoint that handles DTMF inputs.

### 5.Run the code

Execute the code using Node.js:

```sh
node order_confirmation_call/confirmation_call.js
```

### 6. Expected call flow

When the code is executed, the call will follow these steps:

**1.Initial Call to Customer:** The call is initiated to the customer's number first.

**2.Customer Answers Call:** Once the customer answers the call, a prompt for order confimation music plays.

**3.DTMF Handling:** TThe customer presses 1 to confirm the order or presses any other input to cancel the order.

**4.Response Handling:**

- If the customer presses 1, a confirmation music file plays, indicating the order was confirmed.
- If the customer does not press 1 or presses another input, an order cancellation music file plays, indicating the order was canceled.

You can handle these steps programmatically using the Piopiy package. Ensure that your [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L6) are correctly configured, and the [**music_file**](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L9), [**customer_number**](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L11), [**piopiy_number**](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L12) and [**ngrok URL**](https://github.com/telecmi/piopiy_node_example/blob/development/order_confirmation_call/confirmation_call.js#L10) provided are valid.

## Example usage

Replace the placeholders in the code with your actual values:

```javascript
const { Piopiy, PiopiyAction } = require("piopiy");
const express = require("express");
const app = express();
app.use(express.json());

const piopiy = new Piopiy("your_app_id", "your_app_secret");
const action = new PiopiyAction();

const music_file = "https://example.com/your_order_confirmation_music.mp3"; // Your order confimation music file or music file URL
const ngrok_url = "https://ngrok.order.confirmation.io/dtmf"; // Replace with your actual Ngrok URL
const customer_number = "Your customer number"; // Your customer phone number with country code
const piopiy_number = "Your piopiy number"; // Your piopiy number provided by the Piopiy TeleCMI platform
const options = {
  max_digit: 1, // (Optional) Maximum number of digits expected from the user input
  max_retry: 1, // (Optional) Maximum number of retry attempts
  timeout: 1, // (Optional) Time allowed between DTMF inputs in seconds
};

// Initiate the call
action.playGetInput(ngrok_url, music_file, options);

piopiy.voice.call(customer_number, piopiy_number, action.PCMO())
  .then((res) => {
    console.log("Success response:", res);
  })
  .catch((error) => {
    console.error("Error:", error);
  });

// Set up the webhook server
app.post("/dtmf", (req, res) => {
  const action = new PiopiyAction();
  const dtmf = req.body.dtmf; // Assuming DTMF input is in the body of the request

  if (dtmf == 1) {
    // Music to play if customer confirms the order
    action.playMusic("https://example.com/your_confirmation_music.mp3");
  } else {
    // Music to play if customer cancel the order
    action.playMusic("https://example.com/your_order_not_confirmed_music.mp3");
  }
  res.send(action.PCMO());
});

app.listen(3001, () => {
  console.log(`Server is running on port 3001`);
});
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
