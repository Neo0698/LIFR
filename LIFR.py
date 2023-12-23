import asyncio
import websockets
import json


async def send(content):
    async with websockets.connect('ws://quoi29.ddns.net:8765') as websocket:
        # Send a message to the server
       
        await websocket.send(str(content))

        # Receive and print the server's response
        response = await websocket.recv()
       
        return response

def generate(content):
  """
  take one variable:
    dictionnary with the following key:
      "data":text that the LIFR model must use
      
  """
	if(type(content["data"])==str):
		split_text=content["data"].split("\n")
		text=[]
		for el in split_text:
			text.append([el])
		print(text)
		content["data"]=text
	content["type"]="generate"
	text=asyncio.get_event_loop().run_until_complete(send(str(content)))
	return json.loads(text)
def search(content):
  """
  take one variable:
    dictionnary with the following key:
    "ask": and a string in value that correspond to the phrase to search
  """
	content["type"]="search"
	text=asyncio.get_event_loop().run_until_complete(send(json.dumps(content)))
	return text
