import asyncio
import websockets
from piopiy import StreamAction
from asr.deepgram import stream_audio
#from tts.deepgram import set_wss
from tts.elevenlabs import set_wss
from call.piopiy import set_piopiy_ws

global wss
async def handle_client(websocket, path):
    print("Client connected")
    print(f"conn-{id(websocket)}")
    set_wss(websocket)
    set_piopiy_ws(websocket)
    try:
        async for message in websocket:
            if isinstance(message, bytes):
                a =10
                # print(f"Received binary message of {len(message)} bytes")
                # await websocket.send(message)  # Echoing the binary message back
                stream_audio(message)
            else:
                print("Received non-binary message:", message)
              
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e.code} - {e.reason}")
    finally:
        print("Client disconnected")
     


def send_tts_audio(audio_stream_base64):
    # Send the audio stream to the WebSocket
    print(audio_stream_base64)
 


async def main():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("WebSocket server started at ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())

