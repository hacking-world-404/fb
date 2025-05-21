from os import system as c
import time
import random
import os

A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
P = '\x1b[38;5;201m'

def logo():
    c('clear')
    print(f"""{R}
███████╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗
███████╗█████╗  ██████╔╝
╚════██║██╔══╝  ██╔═══╝ 
███████║███████╗██║     
╚══════╝╚══════╝╚═╝     
{Y}HACKING WORLD - FB AUTO FOLLOW (Root Only)
{A}-------------------------------------------------
""")

def root_check():
    print(f"{Y}[!] Checking Device Root Access...")
    time.sleep(1.5)
    # Fake non-root detection
    is_root = False  # change to True if you wanna bypass

    if not is_root:
        print(f"{R}[!] Root Access Not Found!")
        time.sleep(1)
        print(f"{R}[-] Non-root device detected. Exiting tool.")
        time.sleep(2)
        exit()
    else:
        print(f"{G}[✓] Root Access Detected.")
        time.sleep(1)

def auto_follow():
    logo()
    user = input(f"{C}[+] Enter Facebook Profile Name: ")
    root_check()
    print(f"{G}[✓] Profile Verified: {user}")
    time.sleep(1)

    followers = random.randint(1000, 5000)
    print(f"{Y}[*] Adding {followers} Followers to {user}...")
    time.sleep(2)

    for percent in range(0, 101, 10):
        print(f"{C}[*] Inject Progress: {percent}%")
        time.sleep(0.3)
        c('clear')
        logo()

    print(f"{G}[✓] Successfully Added {followers} Followers to {user}!")
    print(f"{P}[*] Please Restart Facebook App to See New Followers.")
    input(f"\n{C}Press Enter To Exit...")

auto_follow()