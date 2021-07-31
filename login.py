#!/bin/python

import os
import sys
import time
import getpass
import requests

x = "R14N"
y = "R14N V1"

def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.002)


def login():
  os.system("clear")
  sp("\033[1;96m       ╔╗   ╔═══╗╔═══╗╔══╗╔═╗ ╔╗")
  sp("       ║║   ║╔═╗║║╔═╗║╚╣─╝║║╚╗║║")
  sp("       ║║   ║║ ║║║║ ╚╝ ║║ ║╔╗╚╝║")
  sp("       ║║ ╔╗║║ ║║║║╔═╗ ║║ ║║╚╗║║")
  sp("       ║╚═╝║║╚═╝║║╚╩═║╔╣─╗║║ ║║║")
  sp("       ╚═══╝╚═══╝╚═══╝╚══╝╚╝ ╚═╝")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mAuthor   \033[1;91m: \033[1;95mR14N")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mInstagram \033[1;91m: \033[1;95mriangaming_yt")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mYouTube  \033[1;91m: \033[1;95mR14N")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mGithub   \033[1;91m: \033[4;92mhttps://github.com/SpamSms2\033[1;0m")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  username = input (" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mUsername:\033[1;92m ")
  password = input (" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mPassword: ")
  if username == x and password == y:
    print(" \033[1;92mberhasil login")
    time.sleep(1)
  else:
    print(" \033[1;91mgagal login")
    time.sleep(1)
    login()

  os.system("python bash.py")
login()
