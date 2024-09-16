# Piopiy Incoming Call

This example shows how to handle an **Incoming Call** from a customer using the Piopiy package.

## Steps to run the code

### 1.Prerequisites

Before you start, ensure you have completed the [ prerequisite steps ](/README.md).

### 2.Configure the call parameters

- Replace the value in the [ Basic Call ](/sdk_example/inbound_call/basic.py) code with your actual values for

  - [**agent_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/inbound_call/basic.py#L11)

  - [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/inbound_call/basic.py#L13)

- Replace the value in the [ Call with PCMO ](/sdk_example/inbound_call/call_with_pcmo.py) code with your actual values for

  - [**music_file**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/inbound_call/call_with_pcmo.py#L22)

  - [**customer_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/inbound_call/call_with_pcmo.py#L11)

  - [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/inbound_call/call_with_pcmo.py#L13)

- Replace the value in the [ Multiple Numbers ](/sdk_example/inbound_call/multiple_numbers.py) code with your actual values for

  - [**multiple_agent_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/inbound_call/multiple_numbers.py#L11)

  - [**piopiy_number**](https://github.com/telecmi/piopiy_python_example/blob/development/sdk_example/inbound_call/multiple_numbers.py#L13)

### 3.Run the code

To execute the outbound call examples, follow the commands below based on which example you want to run:

- For Basic Call:

```bash
python sdk_example/inbound_call/basic.py
```

- For Call with PCMO:

```bash
python sdk_example/inbound_call/call_with_pcmo.py
```

- For Multiple Numbers:

```bash
python sdk_example/inbound_call/multiple_numbers.py
```
