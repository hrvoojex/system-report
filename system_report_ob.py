#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Autor: Hrvoje T.
Created: 15.12.2017.
Last edit: 02.03.2017.
Version: 0.0.2

Uz pomoć CPU-Z programa uzima podatke o OS-u i hardveru i konvertira
datoteku u xml
"""

import ctypes
import socket
import subprocess
import datetime
import ftplib
import os
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():

    ftpserver_ip = input("FTP server IP: ")
    username = input("FTP server username: ")
    password = input("FTP server password: ")

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


    def ftpsend(upload_file):
        try:
            # ftp server running on 'ftpserver_ip' on port 21
            session = ftplib.FTP(ftpserver_ip, username, password)
            file = open(upload_file, 'rb')
            session.storbinary('STOR ' + upload_file, file)
            file.close()
            session.quit()
        except Exception as err:
            with open('error.log', 'w') as ferr:
                print(err)
                ferr.write(str(datetime.datetime.now()))
                ferr.write('\n')
                ferr.write(str(err))
            return None

        with open('OK.log', 'w') as fok:
            fok.write(str(datetime.datetime.now()))
            fok.write(" OK")
            print(str(datetime.datetime.now()), "OK")

    ftpsend(fname)

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
