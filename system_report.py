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


cpuz = "cpuz_x32.exe"
prm = "-html=system-report.html"

# Pozovi CPU-Z i kreiraj html
subprocess.call([cpuz, prm])

