#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,time
from subprocess import Popen,PIPE,check_call
from colorama import Fore, Style
import webbrowser

def colorprint(verbosity, text):
    if verbosity == "fatal":
        print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
    if verbosity == "warn":
        print(Fore.YELLOW + text + Style.RESET_ALL)
    if verbosity == "info":
        print(Style.DIM + Fore.WHITE + text + Style.RESET_ALL)
    if verbosity == "success":
        print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

logo = ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)


def handbook():
    while True:

        check_call(["clear"])
        print (logo)
        colorprint("info", "Burada CTF'ler hakkında bilgi bulabilirsiniz.")
        colorprint("info", "Lütfen bir konu seçiniz:")
        colorprint("info", "1-->Tersine Mühendislik")
        colorprint("info", "2-->Kriptografi")
        colorprint("warn", "9-->Üst menüye dön")
        colorprint("fatal", "0-->Çık")

        choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/handbook"+Style.RESET_ALL+")\n-->")

        if choice == "9":
            return

        elif choice == "0":
            sys.exit()

        elif choice == "1":
            page = os.path.realpath(__file__) + "/../../handbook_files/reverse/reverse.html"
            savout = os.dup(1)
            os.close(1)
            os.open(os.devnull, os.O_RDWR)
            try:
                webbrowser.open('file:///{}'.format(page))
                time.sleep(1)
            finally:
                os.dup2(savout, 1)

        elif choice == "2":
            page = os.path.realpath(__file__) + "/../../handbook_files/crypto/crypto.html"
            savout = os.dup(1)
            os.close(1)
            os.open(os.devnull, os.O_RDWR)
            try:
                webbrowser.open('file:///{}'.format(page))
                time.sleep(1)
            finally:
                os.dup2(savout, 1)

        raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)

if __name__ == "__main__":
    handbook()


