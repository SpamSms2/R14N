#!/bin/python

import os
import sys
import time

def sp(a):
    for e in a + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.002)

def lagi():
    while True:
        f = input("Do You Want To Continue ? [y/n] : ").lower()
        if f == "y":
            menu()
            break
        elif f == "n":
            print("Terima kasih! Bye.")
            sys.exit()
        else:
            print("Input tak sah. Sila cuba lagi.")

def bersih():
    os.system("clear")

def menu():
    bersih()
    print("\033[1;96m+---------------------------------------+")
    print("Author : R14N")
    print("Youtube : R14N")
    print("Instagram : riangaming_yt")
    print("Partner : Mr.1557")
    print("+---------------------------------------+")
    print("\033[1;92m[1] Install Metasploit")
    print("[2] Spam Call (by Mr.1557)")
    print("[3] Hack CCTV")
    print("[4] Tools Installer payload no root")
    print("[5] IP Tracker")
    print("[6] Deface website")
    print("[7] DDos attack")
    print("\033[1;91m[B] Back/Keluar")
    pil = input("\033[1;95mPilih Sesuai Nomor -> ").lower()

    if pil == "1":
        os.system("pkg update && pkg upgrade -y")
        os.system("pkg install git -y")
        os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
        os.system("chmod +x metasploit.sh")
        os.system("./metasploit.sh")
        os.system("./postgresql_ctl.sh start")
        os.system("msfconsole")
        lagi()

    elif pil == "2":
        os.system("pkg update && pkg upgrade -y")
        os.system("pkg install git -y")
        os.system("pkg install python -y")
        os.system("git clone https://github.com/Aldi4321/spam-call")
        lagi()

    elif pil == "3":
        os.system("pkg update && pkg upgrade -y")  # betulkan typo upgrde -> upgrade
        os.system("termux-setup-storage")
        os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
        lagi()

    elif pil == "4":
        os.system("git clone https://github.com/TechnicalMujeeb/tmvenom")
        lagi()

    elif pil == "5":
        os.system("git clone git://github.com/htr-tech/track-ip.git")
        lagi()

    elif pil == "6":
        print("Next update bro")
        lagi()

    elif pil == "7":
        print("Next update bro")
        lagi()

    elif pil == "b":
        print("Keluar program. Terima kasih.")
        sys.exit()

    else:
        print("Salah pilihan, cuba lagi.")
        time.sleep(1)
        menu()

if __name__ == "__main__":
    menu()
