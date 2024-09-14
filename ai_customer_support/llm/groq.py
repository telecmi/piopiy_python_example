
import os
from groq import Groq
from tts.deepgram import get_speech
from call.piopiy import piopiy_call
import asyncio
groq_key=os.environ.get("GROQ_API_KEY")


# Create the Groq client
client = Groq(api_key=groq_key)

# Set the system prompt
system_prompt = {
    "role": "system",
    "content": "“You are Mani, a voice agent for TeleCMI customer support. Answer questions related to business phone systems, cloud PBX, and cloud contact center issues. Keep responses short, precise, and to the point, with no extra details.Only call function transfer_call when customer inform you to talk to human otherwise you handle every qrery without function call or tool call”"
}

#function prompt
tool = tools = [
        {
            "type": "function",
            "function": {
                "name": "transfer_call",
                "description": "Please wait we transfer your call shortly",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_name": {
                            "type": "string",
                            "description": "The team name to connect the call to",
                        }
                    },
                    "required": ["team_name"],
                },
            },
        }
    ]


# Initialize the chat history
chat_history = [system_prompt]


def chat_with_assistant(user_input):

  # Append the user input to the chat history
  chat_history.append({"role": "user", "content": user_input})

  response = client.chat.completions.create(model="llama3-70b-8192",
                                            messages=chat_history,
                                            tools=tools,
                                            tool_choice="auto",
                                            max_tokens=100,
                                            temperature=1.2)
  # Append the response to the chat history
  
  # Print the response
  print("Assistant:", response.choices[0].message.content)
  response_message = response.choices[0].message
  tool_calls = response_message.tool_calls
  if tool_calls:
         print('')
         print(tool_calls)
         chat_history.append({"role": "assistant","content": "Please wait we are transferring your call shortly"})
         get_speech('Please wait we are transferring your call shortly')
         asyncio.run(piopiy_call())
  if response.choices[0].message.content:
      chat_history.append({
      "role": "assistant",
      "content": response.choices[0].message.content
  })
      get_speech(response.choices[0].message.content)