import time
import sys
from pypresence import Presence, exceptions
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
    try:
        choice = input("app1 / app2 ?\t\t")
        if choice in ["app1", "app2"]:
            return choice
        
        else:
            quitting = input("Do you want to quit?")

            if quitting.lower() in ["y", ""]:
                sys.exit()
            
            else:
                return get_mode()
            
    except KeyboardInterrupt:
        print("Closing now...")
        time.sleep(2)
        sys.exit(0)
        
"""
Set the appID, names of image assets to be used, tooltip text.
Supports more parameters like party size, button, details etc.
but this is a simpler version. Maybe we can add them here in 
future with better documentation.
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

"""

"""
def start_activity(rpc, largeImageKey, largeImageText, smallImageKey, smallIamgeText):

    # reset flag when starting activity
    global flag
    flag = 0

    # first fetch the details
    try:
        rpc.connect()
    except exceptions.DiscordNotFound:
        print("\nCould not find Discord installed and running on this machine.\nExiting...")
        time.sleep(4)
        sys.exit(0)
    
    start_time = time.time()    # for logging
    iter = 0                       # for logging

    while True:
        # logs the cycle number in terminal
        iter += 1
        m = iter - 1

        rpc.update(
            large_image = largeImageKey,
            large_text = largeImageText,
            start = start_time,
            small_image = smallImageKey,
            small_text = smallIamgeText)
        
        # prints the cycle number & uptime in minutes
        print(">>>  Running", iter, "=> uptime:", "%.2f" % (((m)*25)/60),"minutes for", largeImageKey)
        
        # updates after every 25 seconds, just to keep process from getting paused
        time.sleep(25)


def stop_activity(rpc):
    rpc.close()

def main():
    while True:
        mode, largeImageKey, largeImageText, smallImageKey, smallIamgeText = set_mode()
        RPC = Presence(mode)
        try:
            start_activity(RPC, largeImageKey, largeImageText, smallImageKey, smallIamgeText)
        
        except KeyboardInterrupt:
            global flag
            flag += 1

            if flag == 2:
                sys.exit(0)

            print("Activity Interrupted...");time.sleep(1);print("Restarting service in 3s")
            stop_activity(RPC)
            time.sleep(3)

if __name__ == "__main__":
    main()