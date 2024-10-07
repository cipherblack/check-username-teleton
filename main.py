# @cipherblack 

import time
import json
from telethon import TelegramClient
from telethon.errors import FloodWaitError
from telethon.tl.functions.account import CheckUsernameRequest

# client information  
api_id = 'api_id' # api-id 
api_hash = 'api_hash'  # api-hash 
phone_number = '+123456789'  # phon-number to login cli-bot
input_file = r'file-name-for-usernames' # input file usernames
output_file = 'available_usernames.json' # output file and read this after end program

client = TelegramClient('username_bot', api_id, api_hash)

async def check_username(username): # func for check username 
    try:
        time.sleep(1.5)
        result = await client(CheckUsernameRequest(username)) # check username and call true or false
        return result
    except FloodWaitError as e:
        print(f"Flood wait error: Need to wait for {e.seconds} seconds.")
        time.sleep(e.seconds + 1)
        return await check_username(username)
    except Exception as e:
        print(f"Error the usernme is incorrect")
        return False

async def main():
    await client.start(phone_number)
    
    usernames = []
    with open(input_file, 'r') as file: # read input file 
        usernames = [line.strip() for line in file]
    
    available_usernames = []

    for username in usernames:
        if await check_username(username):
            available_usernames.append(username)
        time.sleep(1)  # Flood Wait
        
    with open(output_file, 'w') as file: # write output on file
        json.dump(available_usernames, file, indent=4)

    await client.disconnect()

if __name__ == "__main__": # run cli bot
    import asyncio
    asyncio.run(main())
