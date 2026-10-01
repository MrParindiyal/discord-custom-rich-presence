from pypresence import Presence, exceptions
from random import choice, randint
import sys
import time


def generate_region() -> str:
    country_codes = [
        "ae",
        "ar",
        "at",
        "au",
        "bd",
        "be",
        "br",
        "ca",
        "ch",
        "cl",
        "cn",
        "cu",
        "cz",
        "de",
        "dk",
        "eg",
        "es",
        "et",
        "fi",
        "fr",
        "gb",
        "gr",
        "id",
        "ie",
        "il",
        "in",
        "iq",
        "ir",
        "it",
        "jp",
        "kr",
        "mx",
        "ng",
        "nl",
        "no",
        "np",
        "nz",
        "pe",
        "ph",
        "pk",
        "pl",
        "pt",
        "ru",
        "se",
        "sg",
        "th",
        "tr",
        "ua",
        "ug",
        "us",
        "uz",
        "va",
        "ve",
        "vn",
        "ye",
        "za",
    ]
    protocols = ["wg", "ovpn", "ike", "lw", "nl", "v2r", "ss", "l2tp", "sstp", "pptp"]
    net = ["tor", "i2p", "nym", "freenet"]

    return f"{choice(country_codes)}-{choice(protocols)}-{choice(net)}-{randint(1,999):03d}"


def generate_ip(real: bool) -> str:
    if real:
        return f"{randint(50,250)}.{randint(1,255)}.{randint(1,255)}.{randint(1,255)}"

    return f"{choice([10, 100, 200, 185, 138, 146, 156, 206, 3, 69, 169, 5, 51])}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}"


def start_activity(rpc: Presence, largeImageKey: str):

    try:
        rpc.connect()
    except exceptions.DiscordNotFound:
        print("\nCannot find Discord running on this machine.\nExiting...")
        time.sleep(3)
        sys.exit(0)

    start_time = time.time()
    iter = 0
    spin = ["|", "/", "-", "\\"]

    while True:
        rpc.update(
            large_image=largeImageKey,
            start=start_time,
            details=f"Connected to {generate_region()}",
            buttons=[
                {
                    "label": f"Real IP: {generate_ip(real=True)}",
                    "url": "https://files.catbox.moe/81k97o.mp4",
                },
                {
                    "label": f"Mullvad IP: {generate_ip(real=False)}",
                    "url": "https://tinyurl.com/28xr3538",
                },
            ],
        )
        print(largeImageKey, "\\", end="", flush=True)
        for _ in range(170):
            print(f"\b{spin[iter%4]}", end="", flush=True)
            iter += 1
            time.sleep(0.7)


def stop_activity(rpc: Presence):
    rpc.clear()
    rpc.close()


def main():
    while True:
        RPC = Presence(1555102437583626240)
        try:
            start_activity(
                RPC,
                "mullvad",
            )
            time.sleep(1)

        except KeyboardInterrupt:
            stop_activity(RPC)
            try:
                print("Activity Interrupted...")
                time.sleep(1)
                print("Restarting service in 15s")
                time.sleep(15)
            except:
                sys.exit(0)


if __name__ == "__main__":
    main()
