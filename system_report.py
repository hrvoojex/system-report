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


cpuz = "cpuz_x32.exe"
param = "-html=system-report"

# Pozovi CPU-Z i kreiraj htm datoteku
subprocess.call([cpuz, param])

# Pretvori html u xml
with open("system-report.htm") as f:
    soup = BeautifulSoup(f, "html.parser")
with open('system-report.xml', 'w') as g:
    print(soup.prettify(), file=g)
