import requests
import colorama
import os
import time
import sys
from colorama import init, Fore, Style

# init
init(autoreset=True)
# Example Token
# 2092063202:AAELOJdxQSqKHeqaB1Z9dXa5Yg_Q3GJiTog
system = input(f" \n\nEnter your system\n Linux/Termux - 1\n Windows - 2\n -> ")
print( "-" * 45 )
if system == '1':
    try:
        os.system("clear")
    except:
        sys.exit(Fore.LIGHTRED_EX + "error")
if system == '2':
    try:
        os.system("cls")
    except:
        sys.exit(Fore.LIGHTRED_EX + "error")
print(f''' 
{Fore.LIGHTBLUE_EX}                                            
        @@@@@@@       @@@@@@@        @@@@@@@@       
        @@@@@@@       @@@@@@@@       @@@@@@@@       
          @@!         @@!  @@@       @@!            
          !@!         !@   @!@       !@!            
          @!!         @!@!@!@        @!!!:!         
          !!!         !!!@!!!!       !!!!!:         
          !!:         !!:  !!!       !!:            
          :!:    :!:  :!:  !:!  :!:  :!:       :!:  
           ::    :::   :: ::::  :::   ::       :::  
           :     :::  :: : ::   :::   :        :::  
                
                {Fore.LIGHTRED_EX}Telegram Bot Finder
                {Fore.LIGHTRED_EX}By .:Lukas:.                  

''')
TOKEN = input(Fore.LIGHTWHITE_EX + "   Token >> " + Fore.LIGHTGREEN_EX)

get_bot = requests.get(f'https://api.telegram.org/bot{TOKEN}/getMe')
try:
 #tg://user?id=<bot_id> 
 print(f'''
 {Fore.LIGHTWHITE_EX}ID - {Fore.LIGHTGREEN_EX}{get_bot.json()["result"]["id"]}
 {Fore.LIGHTWHITE_EX}Name - {Fore.LIGHTGREEN_EX}{get_bot.json()["result"]["first_name"]}
 {Fore.LIGHTWHITE_EX}Username - {Fore.LIGHTGREEN_EX}@{get_bot.json()["result"]["username"]}
 {Fore.LIGHTWHITE_EX}Can joining groups - {Fore.LIGHTGREEN_EX}{get_bot.json()["result"]["can_join_groups"]}
 {Fore.LIGHTWHITE_EX}Can reading messages in groups - {Fore.LIGHTGREEN_EX}{get_bot.json()["result"]["can_read_all_group_messages"]}
 {Fore.LIGHTWHITE_EX}Inline queries - {Fore.LIGHTGREEN_EX}{get_bot.json()["result"]["supports_inline_queries"]}
 ''')
except:
	sys.exit(f'{Fore.LIGHTRED_EX}      ERROR!       ')
time.sleep(2)
print(Fore.LIGHTRED_EX + "   Press [enter] to exit   ")
input()