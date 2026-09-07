import json
from pypresence import Presence, exceptions
import sys
import time


# application ID (from dev portal)
# replace the string with your own app's ID
# in games.json


"""
We ask user what app they want to run. If any other unexpected
character is used, we assume user wants to exit. In that case, 
we confirm exit with a 'y' or enter key. Other wise we call
the function again to choose an app.
"""


def get_title() -> str | None:
    try:
        game_names = []
        with open("./games.json", "r") as file:
            games = json.load(file)

            for game in games:
                game_names.append(game["title"])

        game_names_str = "/".join(game_names) + "?"

        choice = input(f"{game_names_str}\t")
        if choice in game_names:
            return choice

        else:
            quitting = input("Do you want to quit?")

            if quitting.lower() in ["y", ""]:
                sys.exit()

            else:
                return get_title()

    except KeyboardInterrupt:
        print("Closing now...")
        try:
            time.sleep(2)
        except:
            sys.exit(0)
        sys.exit(0)

    except Exception as e:
        print(f"Unexpected error : {e}")
        sys.exit(0)


"""
Set the appID, names of image assets to be used, tooltip text.
Supports more parameters like party size, button, details etc.
but this is a simpler version. Maybe we can add them here in 
future with better documentation.
"""


def set_mode():
    title = get_title()

    with open("./games.json", "r") as file:
        games = json.load(file)

        for game in games:
            if game["title"] == title:
                appID = game["attr"]["appID"]
                largeimg = game["attr"]["largeimg"]
                largetext = game["attr"]["largetext"]
                smallimg = game["attr"]["smallimg"]
                smalltext = game["attr"]["smalltext"]

                return appID, largeimg, largetext, smallimg, smalltext

    return


# connect discord running on system to the application ID(client ID)
# --------------------------------------

"""

"""


def start_activity(
    rpc: Presence,
    largeImageKey: str,
    largeImageText: str,
    smallImageKey: str,
    smallIamgeText: str,
):

    # first fetch the details
    try:
        rpc.connect()
    except exceptions.DiscordNotFound:
        print("\nCannot find Discord running on this machine.\nExiting...")
        time.sleep(3)
        sys.exit(0)

    # for logging
    start_time = time.time()
    iter = 0

    while True:
        # logs the cycle number in terminal
        iter += 1
        m = iter - 1

        rpc.update(
            large_image=largeImageKey,
            large_text=largeImageText,
            start=start_time,
            small_image=smallImageKey,
            small_text=smallIamgeText,
        )

        # prints the cycle number & uptime in minutes
        print(
            ">>>  Running",
            iter,
            "=> uptime:",
            "%.2f" % (((m) * 25) / 60),
            "minutes for",
            largeImageKey,
        )

        # updates after every 25 seconds, just to keep process from getting paused
        time.sleep(24)


def stop_activity(rpc: Presence):
    rpc.clear()
    rpc.close()


def main():
    while True:
        appID, largeImageKey, largeImageText, smallImageKey, smallIamgeText = set_mode()
        RPC = Presence(appID)
        try:
            start_activity(
                RPC, largeImageKey, largeImageText, smallImageKey, smallIamgeText
            )
            time.sleep(1)

        except KeyboardInterrupt:
            stop_activity(RPC)
            try:
                print("Activity Interrupted...")
                time.sleep(1)
                print("Restarting service in 3s")
                time.sleep(3)
            except:
                sys.exit(0)


if __name__ == "__main__":
    main()
