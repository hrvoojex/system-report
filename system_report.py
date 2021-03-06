#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Autor: Hrvoje T.
Last edit: 15.12.2017.
Version: 0.0.1

Uz pomoć CPU-Z programa uzima podatke o OS-u i hardveru i konvertira
datoteku u xml
"""

import os
import socket
import subprocess
from shutil import copyfile


# Saznaje ime lokacije ili ime računala radi imenovanja datoteke
# Prvo postavi da se file zove kao lokalno računalo
store_name = socket.gethostname()
for root, dirs, files in os.walk("C:\\PCT"):
    # Onda potraži datoteku C:\PCT\ime_prodavaonice.who ako ima pa tako imenuj
    for file in files:
        if file.endswith(".who") or file.endswith(".WHO"):
            # Odsjeci nastavak filea u C:\PCT\store_name.who na samo store_name
            store_name = file[0:-4]

# Varijable programa koji treba izvesti i datoteka u koju se sprema rezultat
cpuz = "cpuz_x32.exe"
param = "-txt=" + store_name
fname = store_name + ".txt"

# Pozovi CPU-Z i kreiraj txt datoteku naziva u 'param' varijabli
subprocess.call([cpuz, param])

# Kopiraj datoteke u C:\PCT\ i u datoteku anketa.txt za slanje na server
try:
    copyfile(fname, 'C:\\PCT\\anketa.txt')
    copyfile(fname, 'C:\\PCT\\' + fname)
except Exception as e:
    pass
