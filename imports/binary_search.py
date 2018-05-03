#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,time
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


def binary_search():

    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "Binary taraması için 'binwalk' tool'u kullanılacaktır.")
        colorprint("info", "Taramada bulunan dosyalar 'foremost' tool'u ile çıkartılacaktır.")

        path = config_get('paths', 'path')
        if path == '':
            colorprint("fatal", "\n\tKaydedilmiş dosya yolu bulunamadı. :(")
            colorprint("fatal","\n\tDevam etmek için dosyanın yolunu girin:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nDosya yolunu daha sonraki işlemleriniz için saklayacağız...\n")

        colorprint("success", "\n[*] "+path+" kullanılıyor\n")
        choice = raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a, yeni dosya yolu girmek için 'p'ye basın..." + Style.RESET_ALL).lower()

        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n--> Yeni dosya yolu: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] "+path+" kullanılıyor\n")

        std = Popen(["binwalk",path], stdout=PIPE,stderr=PIPE)
        (out,err) = std.communicate()

        if not err:
            print(out)

            print("Gömülü dosyaları çıkartmak ister misiniz? E/H\n")
            colorprint("warn", "9-->Üst menüye dön")
            colorprint("fatal", "0-->Çık")

            extract_choice = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n-->").lower()

            if extract_choice == "9":
                return
            elif extract_choice == "0":
                sys.exit()
            elif extract_choice == "y":
                while True:
                    print("\nLütfen çıktı klasörü yolunu belirtin:")
                    colorprint("warn", "İşlemi iptal et -> 9")
                    colorprint("fatal", "Çık -> 0")

                    out_path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/binary_search"+Style.RESET_ALL+")\n--> Output path: ")

                    if out_path == "9":
                        return
                    elif out_path == "0":
                        sys.exit()
                        
                    std = Popen(["foremost",path,"-o",out_path], stdout=PIPE,stderr=PIPE)
                    (out,err) = std.communicate()

                    if out.find("ERROR") == -1:
                        if out_path == '':
                            colorprint("success", "Bulunan dosyalar 'output/' dizinine yazılıyor...\n")
                        else:
                            colorprint("success", "Bulunan dosyalar " + out_path + "dizinine yazılıyor...\n")
                        raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)
                        break
                    else:
                        colorprint("fatal", "Girdiğiniz çıktı yolunda dosya zaten mevcut. Başka bir yol belirtin.")
                        raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)

        else:
            colorprint("fatal", "Böyle bir dosya bulunamadı.\nTekrar başlatılıyor...\n")
            raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)  
                    
if __name__ == "__main__":
    binary_search()


