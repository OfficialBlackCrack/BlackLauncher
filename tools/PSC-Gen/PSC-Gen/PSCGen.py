import random, discord_webhook, time, os, fade, colorama
from discord_webhook import DiscordWebhook, DiscordEmbed


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
        code = random.randint(1000000000000000,9999999999999999)
        os.system("cls")
        print(banner)
        print(f"                     [{green}+{reset}] New Code: {blue}{code}{reset}")
        time.sleep(0.5)
        webhook = DiscordWebhook(url=input_webhook)
        embed = DiscordEmbed(title='PSC Generator', description=f"`➕` Code: {code}", color=random.choice(colors_list))
        webhook.add_embed(embed)
        time.sleep(0.5)
        response = webhook.execute() 
main()
