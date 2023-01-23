import requests
import random
import time
import os
from colorama import Fore

print("         __   __                         ")
print("         \ \ / /                         ")
print("          \ V / ___ _ __ __ _ _____   _  ")
print("          /   \/ __| '__/ _` |_  / | | | ")
print("         / /^\ \__ \ | | (_| |/ /| |_| | ")
print("         \/   \/___/_|  \__,_/___|\__, | ")
print("                                   __/ | ")
print("                                  |___/ \n ")
print("=============================================================\n")
Script = "       Discord Bot Type and Delete Messages\n"
print("Script       : " + Script)
Github = "       https://github.com/xsrazy/Discord-Bot\n"
print("Github       : " + Github)
print("=============================================================\n")
print('PERINGATAN   :        JANGAN DIJUAL, BANGSAT! \n')
print("=============================================================\n")

time.sleep(1)

channel_id = input("Enter Channel ID (Not Server)        :   ")
time2 = int(input("Set the time to send the messages    :   "))
time1 = int(input("Set the time to delete messages      :   "))

time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

with open("message.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
        channel_id = channel_id.strip()

        payload = {
            'content': random.choice(words).strip()
        }

        headers = {
            'Authorization': authorization
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.WHITE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])

        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

        if response.status_code == 200:
            messages = response.json()
            if len(messages) == 0:
                is_running = False
                break
            else:
                time.sleep(time1)

                message_id = messages[0]['id']
                response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
                if response.status_code == 204:
                    print(Fore.GREEN + f'Message sent with ID {message_id} deleted successfully')
                else:
                    print(Fore.RED + f'Failed to delete message with ID {message_id}: {response.status_code}')
        else:
            print(f'Failed to get messages on channel: {response.status_code}')

        time.sleep(time2)
