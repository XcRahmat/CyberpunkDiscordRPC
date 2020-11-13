from pypresence import *
from time import time
from os import system

system("title CyberpunkDiscordRPC")

activity_list = ["Main menu",
                 "Map editor",
                 "Exploring the world",
                 "Beta testing"]

print("Choose an activity to display\n")

for i in activity_list:
    print(f"{activity_list.index(i) + 1} - {i}")

while True:
    try:
        activity_input = int(input("\n>>> "))
        activity = activity_list[activity_input - 1]
        break
    except ValueError and IndexError:
        print("Enter a valid number")

timestamp = int(time())
CLIENT_ID = 776904678688292874
RPC = Presence(CLIENT_ID)
RPC.connect()

RPC.update(start=timestamp,
           large_image="icon",
           large_text="Closed Beta",
           details="In game",
           state=activity)

input("To close the program, press Enter...")
