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

def strings_out(path):
    std = Popen(["strings",path], stdout=PIPE,stderr=PIPE)
    (out,err) = std.communicate()
    return out;

def exiftool_out(path):
    std = Popen(["exiftool",path], stdout=PIPE,stderr=PIPE)
    (out,err) = std.communicate()
    return out;

def searcher(path):

    print("Aranacak flag'ın içerdiği bir keyword giriniz.")
    print("Örnek : CTF_{flag_burda} gibi bir flag için 'CTF' ya da '_{' gibi keywordler uygundur.")
    
    flag_keyword = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")\n-->")

    std = Popen("strings "+path+" | grep -i "+flag_keyword, stdout=PIPE,stderr=PIPE,shell=True)
    (s_out,err) = std.communicate()

    std = Popen("exiftool "+path+" | grep -i "+flag_keyword, stdout=PIPE,stderr=PIPE,shell=True)
    (e_out,err) = std.communicate()

    if s_out+e_out:
        colorprint("success", s_out+e_out)
    else:
        colorprint("fatal", "Keyword bulunamadı. :(")

def metadata_search():

    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "Belirlediğiniz keywordü bulmak için 'exiftool' ve 'strings' kullanılacaktır.")
        
        path = config_get('paths', 'path')
        if path == '':
            colorprint("fatal", "\n\tKaydedilmiş dosya yolu bulunamadı. :(")
            colorprint("fatal","\n\tDevam etmek için dosyanın yolunu girin:\n")
            
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")\n-->")

            config_set('paths', 'path', path)
            colorprint("info", "\nDosya yolunu daha sonraki işlemleriniz için saklayacağız...\n")

        
        colorprint("success", "\n[*] Using "+path+"\n")
        choice = raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a, yeni dosya yolu girmek için 'p'ye basın..." + Style.RESET_ALL).lower()

        if choice == 'p':
            path = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/hash_brute"+Style.RESET_ALL+")\n--> Yeni dosya yolu: ")
            config_set('paths', 'path', path)
            colorprint("success", "\n[*] Using "+path+"\n")

        std = Popen(["file",path], stdout=PIPE,stderr=PIPE)
        (out,err) = std.communicate()
        if out.find("No such file or directory") == -1:

            colorprint("info", "1-->'exiftool' ve 'strings' çıktısında belirli bir keyword için arama yap")
            colorprint("info", "2-->MetaData'yı göster")
            colorprint("info", "3-->Strings çıktısını göster")
            colorprint("warn", "9-->Üst menüye dön")
            colorprint("fatal", "0-->Çık")
            choose = raw_input("Axion TERMINAL("+Style.BRIGHT+Fore.CYAN+"/file_analysis/metadata_search"+Style.RESET_ALL+")\n-->").lower()
            if choose == "1":
                searcher(path)
                raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)
            elif choose == "2":
                colorprint("warn", exiftool_out(path))
                raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)
            elif choose == "3":
                colorprint("warn", strings_out(path))
                raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)
            elif choose == "9":
                return
            elif choose == "0":
                sys.exit()
            else:
                colorprint("fatal", "Yanlış girdi.\nTekrar başlatılıyor...\n")
                raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)
        else:
            colorprint("fatal", "Böyle bir dosya bulunamadı.\nTekrar başlatılıyor...\n")
            raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)
            break
                 
if __name__ == "__main__":
    metadata_search()


