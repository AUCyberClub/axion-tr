#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from subprocess import Popen, PIPE, check_call
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

logo = ("""
    _    __  _____ ___  _   _         _   _   _  ____ ____
   / \   \ \/ /_ _/ _ \| \ | |       / \ | | | |/ ___/ ___|
  / _ \   \  / | | | | |  \| |_____ / _ \| | | | |  | |
 / ___ \  /  \ | | |_| | |\  |_____/ ___ \ |_| | |__| |___
/_/   \_\/_/\_\___\___/|_| \_|    /_/   \_\___/ \____\____|
        """)

morse_table = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '(': '-.--.-',
        '8': '---..',           ')': '-.--.-',
        '9': '----.',           '_': '..--.-',
        ' ': '/',
}

def encode_morse(text_msg):
    morse_msg = ""
    for i in list(text_msg):
        morse_msg = morse_msg + morse_table[i] + " "
    return morse_msg


def morse_encoder():
    check_call(["clear"])
    while True:
        print (logo)
        colorprint("info", "Bu bölümde metin mesajlarını morse alfabesi şeklinde encode edebilirsiniz.")
        colorprint("info", "Mesajı girin:")
        colorprint("warn", "9-->Üst menüye dön")
        colorprint("fatal", "0-->Çık")

        text_msg = raw_input(
            "Axion TERMINAL(" + Style.BRIGHT + Fore.CYAN + "/crypto/morse_encoder" + Style.RESET_ALL + ")\n-->")

        if text_msg == "9":
            return
        elif text_msg == "0":
            sys.exit()
        else:
            morse_msg = encode_morse(text_msg)
            colorprint("success", "Mesajınız dönüştürüldü.")
            print ("Mesaj:\n--> %s" % morse_msg)

        raw_input(Style.DIM + Fore.WHITE + "Devam etmek için Enter'a basın..." + Style.RESET_ALL)

if __name__ == "__main__":
    morse_encoder()