# Piopiy Incoming Call

This example demonstrates how to make an **Outbound Call** using the Piopiy package.

## Steps to run the code

### 1.Prerequisites

Before you start, ensure you have completed the [ prerequisite steps ](/README.md).

### 2.Configure the call parameters

- Replace the value in the [ Basic Call ](/sdk_example/outbound_call/basic.py) code with your actual values for

  - [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/basic.py#L5)

  - [**customer_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/basic.py#L10)

  - [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/basic.py#L9)

  - [**agent_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/basic.py#L8)

- Replace the value in the [ Call with PCMO ](/sdk_example/outbound_call/call_with_pcmo.py) code with your actual values for

  - [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/call_with_pcmo.py#L5)

  - [**music_file**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/call_with_pcmo.py#L27)

  - [**customer_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/call_with_pcmo.py#L11)

  - [**agent_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/call_with_pcmo.py#L13)

  - [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/call_with_pcmo.py#L12)

- Replace the value in the [ Multiple Numbers ](/sdk_example/outbound_call/multiple_numbers.py) code with your actual values for

  - [**app_id** & **app_secret**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/multiple_numbers.py#L5)

  - [**customer_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/multiple_numbers.py#L11)

  - [**multiple_agent_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/multiple_numbers.py#L9)

  - [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/outbound_call/multiple_numbers.py#L10)

### 3.Run the code

To execute the outbound call examples, follow the commands below based on which example you want to run:

- For Basic Call:

```bash
python sdk_example/outbound_call/basic.py
```

- For Call with PCMO:

```bash
python sdk_example/outbound_call/call_with_pcmo.py
```

- For Multiple Numbers:

```bash
python sdk_example/outbound_call/multiple_numbers.py
```
