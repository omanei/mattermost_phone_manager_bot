import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
MATTERMOST_URL = os.getenv("MATTERMOST_URL")
MATTERMOST_API_PATH = os.getenv("MATTERMOST_API_PATH")
MATTERMOST_PORT=os.getenv("MATTERMOST_PORT")
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

def get_config(url: str, token: str):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def save_phone(phone: str, user_id: str):
    token = ADMIN_TOKEN
    
    if token is None:
        return "An error has occurred 😥"
        
    data = get_config(f"{MATTERMOST_URL}:{MATTERMOST_PORT}{MATTERMOST_API_PATH}/config", token)

    new_attributes = {
        'GroupIDs': "",
        'TeamIDs': "",
        'UserIDs': "",
        'Name': "",
    }

    new_attributes["Name"] = str(phone)

    new_attributes["UserIDs"] = [f"{user_id}"]

    data["PluginSettings"]["Plugins"]['com.mattermost.custom-attributes']['customattributes'].append(
        new_attributes)
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"  
    }
    
    
    response = requests.put(f"{MATTERMOST_URL}:{MATTERMOST_PORT}{MATTERMOST_API_PATH}/config/patch", data=json.dumps(data), headers=headers)
    

    if response.status_code == 200:
        return "Number saved 😃"
    else:
        return "An error has occurred 😥"