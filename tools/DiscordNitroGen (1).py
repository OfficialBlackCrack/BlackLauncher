import ctypes
import string
import os
import time
LICNESE = """
made by godclicks#0001 pls do not steal ;)
"""

USE_WEBHOOK = True

print(LICNESE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:
    import requests
except ImportError:
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()
try:
    import numpy
except ImportError:
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()

url = "https://github.com"
try:
    response = requests.get(url)
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()


class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Discord Nitro checker made by godclicks")
        else:
            print(f'\33]0; nitro gen and checker - Made by Godclicks <3\a',
                  end='', flush=True)

        print(""" 
                    _   _ _ _              _____            
                   | \ | (_) |            / ____|           
                   |  \| |_| |_ _ __ ___ | |  __  ___ _ __  
                   | . ` | | __| '__/ _ \| | |_ |/ _ \ '_ \ 
                   | |\  | | |_| | | (_) | |__| |  __/ | | |
                   |_| \_|_|\__|_|  \___/ \_____|\___|_| |_|
                                                            
                                                            
                                                        """)
        time.sleep(2)
        self.slowType("Made by: godclicks", .02)
        time.sleep(1)
        self.slowType(
            "\nInput Wie viel willst du überprüfen und generieren? : ", .02, newLine=False)

        try:
            num = int(input(''))
        except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()

        if USE_WEBHOOK:
            self.slowType(
                "Wenn du die Nitro Infos an eine  Discord webhook senden willst ,schicke hier den link rein oder drücke Enter wenn du es nicht willst : ", .02, newLine=False)
            url = input('')
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(
                        url=url,
                        content=f"```Started checking urls\nI will send any valid codes here```"
                    ).execute()

        valid = []
        invalid = 0 
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break

            except Exception as e:
                print(f" Error | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - godclicks <3")
                print("")
            else:
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by godclicks\a', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")
        input("\nDrücke Enter zum Beenden!")
        [input(i) for i in range(0, 0, -1)]
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def quickChecker(self, nitro:str, notify=None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url=url,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True
        else:
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()