#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
from imports.find_file_ext import find_file_ext
from imports.binary_search import binary_search
from imports.metadata_search import metadata_search
from imports.hash_ident import hash_ident
from imports.hash_extractor import hash_extractor
from imports.hash_brute import hash_brute
from imports.morse_decoder import morse_decoder
from imports.morse_encoder import morse_encoder
from imports.pdf_parser import pdf_parser
from imports.vigenere_decoder import vigenere_decoder
from imports.xor_decoder import xor_decoder
from imports.base64_decoder import base64_decoder
from imports.bin_hex_dec_ascii import bin_hex_dec_ascii
from imports.rot13_caesar import rot13_caesar
from imports.qr_decoder import qr_decoder
from imports.volatility_info import volatility_info
from imports.volatility_notepad import volatility_notepad
from imports.volatility_pslist import volatility_pslist
from imports.volatility_screenshot import volatility_screenshot
from imports.volatility_cmdscan import volatility_cmdscan
from imports.volatility_iehistory import volatility_iehistory
from imports.ini_edit import config_get, config_set
from imports.handbook import handbook


from colorama import Fore, Style
def colorprint(verbosity, text):
    if verbosity == "fatal":
        print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)
    if verbosity == "warn":
        print(Fore.YELLOW + text + Style.RESET_ALL)
    if verbosity == "info":
        print(Style.DIM + Fore.WHITE + text + Style.RESET_ALL)
    if verbosity == "success":
        print(Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL)

import readline, glob
class tab_completer(object):
    def path_completer(self, text, state):
        return [x for x in glob.glob(text + '*')][state]
def auto_path_completer():
    tc = tab_completer()

    readline.set_completer_delims('\t')
    readline.parse_and_bind("tab: complete")

    readline.set_completer(tc.path_completer)

logo = ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)


def file_analysis():
    while True:
        os.system('clear')
        print (logo)

        print("Seçenekler:")
        colorprint("info", "1-->Dosya türünü bul")
        colorprint("info", "2-->Dosyanın içinde gizlenmiş dosyaları ara")
        colorprint("info", "3-->Dosyanın MetaData'sında ve binary'sinde arama yap")
        colorprint("info", "4-->PDF dosyası ayrıştırıcı ve analizi")
        colorprint("warn", "9-->Üst menüye dön")
        colorprint("fatal", "0-->Çık")

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/file_analysis" + Style.RESET_ALL + ")\n-->")

        if choice == 1:
            find_file_ext()
        elif choice == 2:
            binary_search()
        elif choice == 3:
            metadata_search()
        elif choice == 4:
            pdf_parser()
        elif choice == 9:
            main_menu()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", "Yanlış girdi tekrar deneyin...")


def crypto():
    while True:
        os.system('clear')
        print (logo)

        print("Seçenekler:")
        colorprint("info", "1-->Elimdeki string hash olabilir mi türü nedir?")
        colorprint("info", "2-->Zip, Rar, TrueCrypt kaba kuvvet saldırısı")
        colorprint("info", "3-->Hash kaba kuvvet saldırısı")
        colorprint("info", "4-->Vigenere çözücü")
        colorprint("info", "5-->Morse çözücü")
        colorprint("info", "6-->Morse oluşturucu")
        colorprint("info", "7-->XOR çözücü")
        colorprint("info", "8-->Base64 çözücü")
        colorprint("info", "10-->Bin,Hex,Dec ve ASCII dönüştürücüler")
        colorprint("info", "11-->Caesar ve ROT şifre çözücü")
        colorprint("info", "12-->QRCode okuyucu")
        colorprint("warn", "9-->Üst menüye dön")
        colorprint("fatal", "0-->Çık")

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto" + Style.RESET_ALL + ")\n-->")

        if choice == 1:
            hash_ident()
        elif choice == 2:
            hash_extractor()
        elif choice == 3:
            hash_brute()
        elif choice == 4:
            vigenere_decoder()
        elif choice == 5:
            morse_decoder()
        elif choice == 6:
            morse_encoder()
        elif choice == 7:
            xor_decoder()
        elif choice == 8:
            base64_decoder()
        elif choice == 10:
            bin_hex_dec_ascii()
        elif choice == 11:
            rot13_caesar()
        elif choice == 12:
            qr_decoder()
        elif choice == 9:
            main_menu()
        elif choice == 0:
            sys.exit()
        else:

            colorprint("fatal", "Yanlış girdi tekrar deneyin...")

def ram():
    while True:
        os.system('clear')
        print (logo)

        print("Seçenekler:")
        colorprint("info", "1-->Ram dump işletim sistemi bul")
        colorprint("info", "2-->Ram dump notdefteri oku")
        colorprint("info", "3-->Ram dump process listele")
        colorprint("info", "4-->Ram dump screenshot çek")
        colorprint("info", "5-->Ram dump CMD komut görüntüle")
        colorprint("info", "6-->Ram dump Internet Explorer geçmişi görüntüle")
        colorprint("warn", "9-->Üst menüye dön")
        colorprint("fatal", "0-->Çık")

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/ram_analysis" + Style.RESET_ALL + ")\n-->")

        if choice == 1:
            volatility_info()
        elif choice == 2:
            volatility_notepad()
        elif choice == 3:
            volatility_pslist()
        elif choice == 4:
            volatility_screenshot()
        elif choice == 5:
            volatility_cmdscan()
        elif choice == 6:
            volatility_iehistory()
        elif choice == 9:
            main_menu()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", "Yanlış girdi tekrar deneyin...")


def main_menu():
    while True:
        os.system('clear')
        print ("""
                                               ░░▒█░░░░       ░░░░░░     ░░░▓█░░
                                                ░░████░░░ ░░░░█████▓░░░░░████░░
                                                ░░▓░░▒███▒███████████░▒███░░░▒
                                                ░░▓░ ░░████░░░▓▓▓███████░░  ░▓░
                                           ░░░░░░██░░░░▒███████████████▒░░░░▓▒
                              ░░  ░░░░░░░░▒███▓░░░█░▓█████████████████████▓░█░░
                   ░░░  ░  ░░░░░░░▒████▒░░░░░░░░░░█▒███████████████████████░█░
               ░░░░░░░░▒▓████████████████████████████████████████████████████░
               ░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░  ░░░████▒████████████▒████▒████░░░
              ░░███████░██▒░░██░███████░███████▓░██████░░░░░███████░░░░░██████░░
              ░███░███████░░███▓██░░▓██▒██░░▒██░░████████████████████████▒▓███░░
              ░████▓██▒██▓░░██▒██▓░░░░░███░░    ░░███████████▓░░░████████████░░
            ░░▒██░░░██▒███████▒██▒▒▒▒░░██▒▒▒▒░░ ░░▓█████████████████████████▒░
            ░░███░░▓█▓███████░▒███▓█▓█▒███▓░░░░ ░░░▒░█████████▒░▓█████████░░░░
            ░░░░░░░▓██████▒░░▒▒▓▓▓▒██░█▓███████████████████████████████▒░░░░░
                  ░░░░░██████░░░░░▒██▓▓░░ ░ ░░░ ░░░░░░░░░██▓███████▓██░░
                        ░░▓██████████░░                  ░░░░█████░░░░
                           ░░░░░░░░░░░░                     ░░▒█▓░░
                    _    __  _____ ___  _   _         _   _   _  ____ ____
                   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
                  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
                 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
                /_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
                          ██------->CTF Toolkit Project<--------██
        """)
        print("Lütfen birini seçiniz:")
        colorprint("info", "1-->Dosya Analizi")
        colorprint("info", "2-->Kripto ve Şifreleme")
        colorprint("info", "3-->RAM Dump Analizi")
        colorprint("info", "4-->Rehber")
        colorprint("fatal", "0-->Çık")

        choice = input("Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/" + Style.RESET_ALL + ")\n-->")
        if choice == 1:
            file_analysis()
        elif choice == 2:
            crypto()
        elif choice == 3:
            ram()
        elif choice == 4:
            handbook()
        elif choice == 0:
            sys.exit()
        else:
            colorprint("fatal", "Yanlış girdi tekrar deneyin...")


if __name__ == "__main__":
    os.system('clear')
    auto_path_completer()

    config_set('paths', 'path', '')
    colorprint("info", "\nEğer bir dosya üzerinde işlem yapacaksanız dosya yolu belirtiniz, aksi halde 'c' ye basınız.")
    choice = raw_input("\nAxion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/"+Style.RESET_ALL+")\n-->")

    if choice is not 'c':
        config_set('paths', 'path', choice)
        colorprint("info", "Dosya yolunu daha sonraki işlemleriniz için saklayacağız...\n")
        
    try:
        main_menu()
    except KeyboardInterrupt:
        colorprint("fatal", "\nProgram Kapanıyor..!")
        sys.exit()
