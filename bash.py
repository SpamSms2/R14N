#!/bin/python

import os,sys,time
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.002)
def lagi():
    f = input("Do You Want To Continue ? [y/n] : ")
    if f == "y":
        os.system("python bash.py")
    elif f == "n":
         sys.exit()



def bersih():
   os.system("clear")

def menu():
    bersih()
    print ("\033[1;96m+---------------------------------------+")
    print ("Author : R14N")
    print ("Youtube : R14N")
    print ("Instagram : riangaming_yt")
    print ("Partner : Mr.1557") 
    print ("+---------------------------------------+")
    print ("\033[1;92m[1]Install Metasploit")
    print ("[2]Spam Call (by Mr.1557)")
    print ("[3]Hack CCTV")
    print ("[4]Tools Instaler payload no root")
    print ("[5]IP Tracker")
    print ("[6]Deface website")
    print ("[7]DDos attack")
    print ("\033[1;91m[B]Back/Keluar")
    pil = input ("\033[1;95mPilih Sesuai Nomor -> ")
    if pil =="1":
       os.system("pkg update && pkg upgrade")
       os.system("pkg install git")
       os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
       os.system("chmod +x metasploit.sh")
       os.system("./metasploit.sh")
       os.system("./postgresql_ctl.sh start")
       os.system("msfconsole")
       lagi()
    elif pil =="2":
       os.system("pkg update && pkg upgrade")
       os.system("pkg install git")
       os.system("pkg install python")
       os.system("git clone https://github.com/Aldi4321/spam-call")
       lagi()
    elif  pil =="3":
       os.system("pkg update && pkg upgrde")
       os.system("termux-setup-storage")
       os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
       lagi()
    elif pil =="4":
       os.system("git clone https://github.com/TechnicalMujeeb/tmvenom")
       lagi()
    elif pil =="5":
       os.system("git clone git://github.com/htr-tech/track-ip.git")
       lagi()
    elif pil =="6":
        print ("next update bro")
    elif pil =="7":
        print ("next update bro")
    elif pil =="B":
       lagi()
       sys.exit()
    else:
       print ("salah bang")
       time.sleep(1)
       os.system("python bash.py")
menu()

