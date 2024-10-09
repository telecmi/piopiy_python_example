import requests
import base64
import os
import asyncio
import json
from piopiy import StreamAction


ELEVEN_URL = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL/stream?output_format=mp3_22050_32"
ELEVEN_API_KEY = os.getenv("EL_API_KEY")


def get_speech(text):
    payload = {
     "text": text,
     "voice_id": "EXAVITQu4vr4xnSDxMaL",
     "voice_settings": {"stability":0.1,"similarity_boost": 0.85}
     }

 
    print(ELEVEN_API_KEY)
    headers = {
      "xi-api-key": ELEVEN_API_KEY,
      "content-type": "application/json"
     }
    

    TARGET_CHUNK_SIZE = 50 * 1024 
   
    response = requests.post(ELEVEN_URL, headers=headers, json=payload, stream=True)
    print(response)
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
    
    await sales_agent_ws.send(stream_action.playStream(audio_base64=b64_audio_chunk,audio_type="mp3",sample_rate=8000))
    
    
def set_wss(ws):
    global sales_agent_ws
    sales_agent_ws = ws
  