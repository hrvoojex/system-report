#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Autor: Hrvoje T.
Last edit: 15.12.2017.
Version: 0.0.1

Uz pomoć CPU-Z programa uzima podatke o OS-u i hardveru i konvertira
datoteku u xml
"""

import subprocess
from bs4 import BeautifulSoup
import os


# Saznaje ime lokacije ili ime računala radi imenovanja datoteke
for root, dirs, files in os.walk("C:\PCT"):
    for file in files:
        if file.endswith(".who"):
            #print(os.path.join(root, file))
            # Odsjeci nastavak filea u C:\PCT\store_name.who na samo store_name
            store_name = file[0:-4]

cpuz = "cpuz_x32.exe"
param = "-html=" + store_name

# Pozovi CPU-Z i kreiraj htm datoteku naziva u 'param' varijabli
subprocess.call([cpuz, param])

# Pretvori html u xml
with open(store_name + ".htm") as f:
    soup = BeautifulSoup(f, "html.parser")
with open(store_name + ".xml", 'w') as g:
    print(soup.prettify(), file=g)
