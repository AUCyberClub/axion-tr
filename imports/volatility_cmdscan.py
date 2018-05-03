#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen,PIPE,check_call
from colorama import Fore, Style
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

def volatility_cmdscan():

    while True:

        check_call(["clear"])
        print (logo)
        colorprint("info","RAM dump cmd'de çalışan komutları görüntülemek için 'volatility' tool'u kullanılacaktır.")
        
        path = config_get('paths', 'path')
        if path == '':
            colorprint("fatal", "\n\tKaydedilmiş dosya yolu bulunamadı. :(")
            colorprint("fatal","\n\tDevam etmek için dosyanın yolunu girin:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/ram_analysis/volatility_cmdscan"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nDosya yolunu daha sonraki işlemleriniz için saklayacağız...\n")

        colorprint("success", "\n[*] "+path+" kullanılıyor\n")

        colorprint("warn","9-->Üst menüye dön")
        colorprint("fatal","0-->Çık")

        choice = raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a, yeni dosya yolu girmek için 'p'ye basın..." + Style.RESET_ALL).lower()

        if choice == "9":
            return
        elif choice == "0":
            sys.exit()
        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/ram_analysis/volatility_cmdscan"+Style.RESET_ALL+")\n--> Yeni dosya yolu: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] "+path+" kullanılıyor\n")

        colorprint("warn", "Lütfen bekleyin...")

        std = Popen("volatility -f " + path + " imageinfo | grep Suggested | cut -d ',' -f1 | cut -d ':' -f2", shell=True, stdout=PIPE,stderr=PIPE)
        (out, err) = std.communicate()

        if err.find("The requested file doesn't exist") != -1:
            colorprint("fatal" ,err)

        else:
            out = out.rstrip()

            if out.find("No") != -1:
                colorprint("warn", out)
                colorprint("fatal", "Dosya, RAM Dump dosyası değil. Yeniden başlatılıyor...")

            else:
                std = Popen("volatility -f " + path + " --profile" + out + " cmdscan", shell=True, stdout=PIPE,stderr=PIPE)
                (out, err) = std.communicate()

                colorprint("success", out)

        raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)

if __name__ == "__main__":
    volatility_cmdscan()