
import os
from groq import Groq
from tts.deepgram import get_speech

groq_key=os.environ.get("GROQ_API_KEY")


# Create the Groq client
client = Groq(api_key=groq_key)

# Set the system prompt
system_prompt = {
    "role": "system",
    "content": "“You are Angel, a voice agent for TeleCMI handling pre-sales. Answer questions related to business phone systems, cloud PBX, and cloud contact center solutions. Keep responses short, precise, and to the point, with no extra details.”"
}

#function prompt
function_prompt = {
    "role": "system",
    "content": "“You are Angel, a voice agent for TeleCMI handling pre-sales. Answer questions related to business phone systems, cloud PBX, and cloud contact center solutions. Keep responses short, precise, and to the point, with no extra details.”"
}

# Initialize the chat history
chat_history = [system_prompt]


def chat_with_assistant(user_input):

  # Append the user input to the chat history
  chat_history.append({"role": "user", "content": user_input})

  response = client.chat.completions.create(model="llama3-70b-8192",
                                            messages=chat_history,
                                            max_tokens=100,
                                            temperature=1.2)
  # Append the response to the chat history
  chat_history.append({
      "role": "assistant",
      "content": response.choices[0].message.content
  })
  # Print the response
  print("Assistant:", response.choices[0].message.content)

  if response.choices[0].message.content:
     get_speech(response.choices[0].message.content)