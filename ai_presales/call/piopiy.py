import os
from piopiy import RestClient,Action


app_id = os.getenv("PIOPIY_APP_ID")
app_secret = os.getenv("PIOPIY_APP_SECRET")

piopiy = RestClient(int(app_id), app_secret)


def make_call(agent_no,piopiy_no,ws_url):
   
   try:
        stream_action = Action()
        stream_action.stream(ws_url)
        # Make the call
        response = piopiy.voice.call(agent_no,piopiy_no,stream_action.PCMO())
        return response
   except Exception as error:
        return error
