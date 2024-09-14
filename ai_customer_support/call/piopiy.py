import os
from piopiy import StreamAction


def set_piopiy_ws(ws):
    # Set the Piopiy API key
    global piopiy_ws
    piopiy_ws = ws

async def piopiy_call():
    # Create the Piopiy client
    action = StreamAction()
    action.call([9198, 9198],9112,{'loop': 2, 'record': True })
    if piopiy_ws:
        await piopiy_ws.send(action.PCMO())