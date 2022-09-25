import aiohttp
import json

from dotenv import load_dotenv
import os
load_dotenv()
apikey = os.getenv('APIKEY')

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': apikey, 
}
dummypayload = {
    "collection": "flicmembers",
    "database": "test",
    "dataSource": "Cluster0"
}

async def find(filt : dict) -> dict:
    newpayload = dummypayload
    newpayload['filter'] = filt
    payload = json.dumps(newpayload)

    async with aiohttp.ClientSession() as session:
        async with session.post(url = 'https://data.mongodb-api.com/app/data-mkxfx/endpoint/data/v1/action/findOne', data = payload, headers=headers) as response:
            html = await response.json()
            return(html['document'])

async def update(filt:dict, update : dict ) ->None:
    newpayload = dummypayload
    newpayload['update'] = update
    newpayload['filter'] = filt
    payload = json.dumps(newpayload)

    async with aiohttp.ClientSession() as session:
        async with session.post(url = 'https://data.mongodb-api.com/app/data-mkxfx/endpoint/data/v1/action/updateOne', data = payload, headers=headers) as response:
            return