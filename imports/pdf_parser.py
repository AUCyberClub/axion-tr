#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import subprocess
from colorama import Fore, Style
from subprocess import Popen,PIPE
from ini_edit import config_get, config_set

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

def func(path):
    while True:
        os.system('clear')
        print (logo)

        colorprint("info", "1-->PDF'in içeriği hakkında bilgi")
        colorprint("info", "2-->PDF'in içine gömülü dosya hakkında bilgi")
        colorprint("warn", "9-->Üst menüye dön")
        colorprint("fatal","0-->Çık")

        choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/pdf_parser"+Style.RESET_ALL+")-->")
        
        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        elif choice == "1":

            std = Popen(["python imports/pdf-parser.py "+path+" | grep /ProcSet"], stdout=PIPE,stderr=PIPE,shell=True)
            
            (s_out,err) = std.communicate()
            if s_out:
                colorprint("success", s_out)
            if err:
                colorprint("fatal", err)

            raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)

        elif choice == "2":
            std = Popen(["python imports/pdf-parser.py -s Embeddedfile --raw --filter "+path+" | grep PDF"], stdout=PIPE,stderr=PIPE,shell=True)
            
            (s_out,err) = std.communicate()
            if s_out:
                colorprint("success", s_out)
            elif err:
                colorprint("fatal", err)
            else:
                colorprint("warn", "\n\tGömülü dosya bulunamadı.\n")

            raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)

def pdf_parser():
    while True:
        os.system('clear')
        print (logo)

        path = config_get('paths', 'path')
        if path == '':
            colorprint("fatal", "\n\tKaydedilmiş dosya yolu bulunamadı. :(")
            colorprint("fatal","\n\tDevam etmek için dosyanın yolunu girin:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/find_file_ext"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nDosya yolunu daha sonraki işlemleriniz için saklayacağız...\n")

        colorprint("success", "\n[*] "+path+" kullanılıyor\n")
        
        colorprint("warn", "9-->Üst menüye dön")
        colorprint("fatal","0-->Çık")

        choice = raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a, yeni dosya yolu girmek için 'p'ye basın..." + Style.RESET_ALL).lower()

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/hash_brute"+Style.RESET_ALL+")\n--> Yeni dosya yolu: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] "+path+" kullanılıyor\n")

        std = Popen(["python", "imports/pdf-parser.py", path], stdout=PIPE,stderr=PIPE)
        (out,err) = std.communicate()

        if out.find("No such file or directory") == -1:
            func(path)
        else:
            colorprint("fatal", "Böyle bir dosya bulunamadı.\nTekrar başlatılıyor...\n")

if __name__ == "__main__":
    pdf_parser()
