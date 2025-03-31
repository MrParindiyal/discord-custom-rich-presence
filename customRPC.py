import time
import sys
from pypresence import Presence
# import random

# to check exit or rerun mode
flag = 0 

# application ID (from dev portal)
# replace the string with your own app's ID

app1ID = '10ZXXXYYYXXXYYYZZ86' # sampleID1
app2ID = '10ZXXXYYYXXXYYYZZ86' # sampleID2
# don't forget, IT'S A STRING, not an int !!


"""
We ask user what app they want to run. If any other unexpected
character is used, we assume user wants to exit. In that case, 
we confirm exit with a 'y' or enter key. Other wise we call
the function again to choose an app.
"""
def get_mode():
    choice = input("app1 / app2 ?\t\t")
    if choice in ["app1", "app2"]:
        return choice
    
    else:
        quitting = input("Do you want to quit?")

        if quitting.lower() in ["y", ""]:
            sys.exit()
        
        else:
            get_mode()

        
"""

"""
def set_mode():
    mode = get_mode()

    # TODO
    # maybe this would be cleaner if implemented as a dict... Maybe   
    if mode == "app1":
        mode = app1ID                   # app ID
        largeimg = "BigImageName1"      # name of asset from dev portal 
        largetxt = "This is App 1"      # tooltip text for large image
        smallimg = "SmallImageName1"    # name of asset from dev portal    
        smalltext = "This is Username"  # tooltip text for small image

    elif mode == "app2":
        mode = app2ID                   # app ID
        largeimg = "BigImageName2"      # name of asset from dev portal 
        largetxt = "This is App 2"      # tooltip text for large image
        smallimg = "__"                     # if asset is not found, then
        smalltext = "__"                    # it won't simply render

    return mode, largeimg, largetxt, smallimg, smalltext



# connect discord running on system to the application ID(client ID)
# --------------------------------------
# RPC=Presence(client_id)

def start_activity():
    RPC = Presence(mode)
    RPC.connect()
    mode, largeImageKey, largeImageText, smallImageKey, smallIamgeText = set_mode()

    start_time = time.time()    # for logging
    n = 0                       # for logging

    while True:
        # logs the cycle number in terminal
        n = n + 1
        m = n - 1
        RPC.update(
            large_image = largeImageKey,
            large_text = largeImageText,
            start = start_time,
            small_image = smallImageKey,
            small_text = smallIamgeText)
        
        # prints the cycle number & uptime in minutes
        print(">>>  Running", n, "=> uptime:", "%.2f" % (((m)*25)/60),"minutes for", largeImageKey)
        
        # updates after every 25 seconds
        time.sleep(25)

def main():
    try:
        start_activity()
    
    except KeyboardInterrupt:
        print("Activity Interrupted...");time.sleep(1);print("Restarting service in 5s")
        time.sleep(5)
        
        if flag:
            sys.exit(0)
        
        flag += 1
        start_activity()

if __name__ == "__main__":
    main()