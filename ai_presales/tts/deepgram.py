import requests
import base64
import os
import asyncio
import json
from piopiy import StreamAction


DEEPGRAM_URL = "https://api.deepgram.com/v1/speak?model=aura-asteria-en&encoding=linear16&sample_rate=8000"
DEEPGRAM_API_KEY = os.getenv("DG_API_KEY")


def get_speech(text):
    payload = {
     "text": text,
     }

    headers = {
          "Authorization": f"Token {DEEPGRAM_API_KEY}",
          "Content-Type": "application/json"
     }

    

    TARGET_CHUNK_SIZE = 50 * 1024 
   
    response = requests.post(DEEPGRAM_URL, headers=headers, json=payload, stream=True)
     
    if response.status_code == 200:
      
        accumulated_chunk = b""
        # Iterate over the response content in chunks
        for chunk in response.iter_content(chunk_size=1020):
            if chunk:
                
                # Accumulate chunks
                accumulated_chunk += chunk
                # If accumulated_chunk reaches or exceeds the target size, process it
                if len(accumulated_chunk) >= TARGET_CHUNK_SIZE:
                    asyncio.run(send_audio_stream(accumulated_chunk[:TARGET_CHUNK_SIZE]))  # Send the 400KB chunk
                    accumulated_chunk = accumulated_chunk[TARGET_CHUNK_SIZE:]  # Keep any remaining data

        # Process each chunk and stream it immediately
        if accumulated_chunk:
            asyncio.run(send_audio_stream(accumulated_chunk))

async def send_audio_stream(audio_stream):
    
    stream_action = StreamAction()
    b64_audio_chunk = base64.b64encode(audio_stream).decode('utf-8')
    
    await sales_agent_ws.send(stream_action.playStream(audio_base64=b64_audio_chunk,audio_type="raw",sample_rate=8000))
    
    
def set_wss(ws):
    global sales_agent_ws
    sales_agent_ws = ws
  