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