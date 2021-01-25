#imports

import colorama
import random
import os
import requests
import time

#start-engine

colorama.init()
os.system('cls')
print("welcome to xbox nitro generator"); time.sleep(2)
os.system('cls')

#hot-keys

def Clear():
    os.system('cls')

def Interval():
    time.sleep(10)

#main-code

def logo():
    print("""
    
██╗░░██╗██████╗░░█████╗░██╗░░██╗  ███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗
╚██╗██╔╝██╔══██╗██╔══██╗╚██╗██╔╝  ████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║
░╚███╔╝░██████╦╝██║░░██║░╚███╔╝░  ██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
░██╔██╗░██╔══██╗██║░░██║░██╔██╗░  ██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
██╔╝╚██╗██████╦╝╚█████╔╝██╔╝╚██╗  ██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║
╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝
                                       made by fighter x""")
    
    print("""
    [1] generate codes
    [2] check out makers youtube
    [3] instructions
    [4] exit
    """)
    choice = int(input("[?]: "))
    if choice == 1:
        codeLen = 24
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
        lp = int(input("Enter The Number Of Unchecked xbox nitros You Need: "))
        k = open('xboxcodes.txt', 'w')
        for i in range(lp):
            k.write("https://discord.com/billing/promotions/xbox-game-pass/redeem/" + ''.join(random.choice(letters) for i in range(codeLen)) + '\n')
        k.close()
        Clear()
        logo()
    
    elif choice == 2:
        r = requests.get('http://youtube.com/c/fighterxofficialyt')
        print(r.url + " --> subscribe now!!!")
        Interval()
        Clear()
        logo()

    elif choice == 3:
        os.system('type readme.txt')
        Interval()
        Clear()
        logo()

    elif choice == 4:
        x = 4

#program-starter

logo()



    

    

