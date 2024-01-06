#!/usr/bin/python3
import os
import json
import requests
from sys import exit
from time import sleep
import macvendors # kütüphanesi, bir MAC (Media Access Control) adresinin sahibi olan şirketi veya üreticiyi belirlemek için kullanılır. Her bir MAC adresinin üçüncü oktetinde (altıncı karakterden önce) bir üretici kimliği bulunur. Bu kimlik, üreticinin MAC adres bloğunu temsil eder.
import getpass
import sys
import time

import uuid 

try:
    from colorizor import *

except ImportError as ier:
    print(ier)

os.system('clear')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.130 / 100)

def slowprint2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.100 / 100)

def slowprint3(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04 / 100)



def show_options():
    slowprint2(f'''

{COLOR.BRIGHT_BLUE} [1] {COLOR.LIGHT_GREEN} hide my ip once
{COLOR.BRIGHT_BLUE} [2] {COLOR.LIGHT_GREEN} hide my ip repeatedly
{COLOR.BRIGHT_BLUE} [3] {COLOR.LIGHT_GREEN} change ip
{COLOR.BRIGHT_BLUE} [4] {COLOR.LIGHT_GREEN} change my mac address
{COLOR.BRIGHT_BLUE} [5] {COLOR.LIGHT_GREEN} do it all
{COLOR.BRIGHT_BLUE} [6] {COLOR.LIGHT_GREEN} show ip
{COLOR.BRIGHT_BLUE} [7] {COLOR.LIGHT_GREEN} stop
{COLOR.BRIGHT_BLUE} [8] {COLOR.LIGHT_GREEN} clear
{COLOR.BRIGHT_BLUE} [9] {COLOR.LIGHT_GREEN} exit/quit
{COLOR.BRIGHT_BLUE} [10]{COLOR.LIGHT_GREEN} show ip_2
{COLOR.BRIGHT_BLUE} [11]{COLOR.LIGHT_GREEN} show ip_3\n

''')    



def show_mac_options():
    slowprint3(f'''
{COLOR.BRIGHT_BLUE}[1]  {COLOR.WHITE}[ Full Random MAC Address ]
{COLOR.BRIGHT_BLUE}[2] {COLOR.WHITE} [ Samsung ]
{COLOR.BRIGHT_BLUE}[3] {COLOR.WHITE} [ Apple ]
{COLOR.BRIGHT_BLUE}[4] {COLOR.WHITE} [ HUAWEI ]
{COLOR.BRIGHT_BLUE}[5] {COLOR.WHITE} [ Nokia ]
{COLOR.BRIGHT_BLUE}[6] {COLOR.WHITE} [ BlackBerry ]
{COLOR.BRIGHT_BLUE}[7] {COLOR.WHITE} [ Motorola ]
{COLOR.BRIGHT_BLUE}[8] {COLOR.WHITE} [ HTC ]
{COLOR.BRIGHT_BLUE}[9] {COLOR.WHITE} [ Google ]
{COLOR.BRIGHT_BLUE}[10] {COLOR.WHITE}[ ASUS ]
{COLOR.BRIGHT_BLUE}[11] {COLOR.WHITE}[ FUJITSU ]
{COLOR.BRIGHT_BLUE}[12] {COLOR.WHITE}[ TOSHIBA ]
{COLOR.BRIGHT_BLUE}[13] {COLOR.WHITE}[ Acer ]
{COLOR.BRIGHT_BLUE}[14] {COLOR.WHITE}[ Dell ]
{COLOR.BRIGHT_BLUE}[15] {COLOR.WHITE}[ HP ]\n
{COLOR.BRIGHT_BLUE}[S] {COLOR.WHITE} Show MAC Adress
{COLOR.BRIGHT_BLUE}[B] {COLOR.WHITE} Back to the main options
{COLOR.BRIGHT_BLUE}[X] {COLOR.WHITE} exit/quit\n
    ''')



def banner():
    slowprint(COLOR.RED + F"""
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⣾⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢤⣄⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠿⠋⠙⠛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⠖⠁⠹⣇⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢿⠏⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀⠀⣿⡀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠏⡇⠀⠀⠀⠀⠀⢹⡄⢀⣴⠒⠲⠤⣤⣤⡤⢞⡽⠃⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⡙⢦⣀⡀⠀⠀⠘⠻⢄⡀⢸⠀⠀⠀⢸⡇⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠸⣇⠀⡀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠹⣟⢦⠀⠀⠀⠀⠹⣼⠀⠀⠀⣼⡇⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣧⠀⢹⡀⠳⣄⣀⣀⣠⠖⠋⠉⠲⠇⠀⠘⢿⢷⠀⠀⠙⡄⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⢸⠀⠀⠇⣠⡄⠉⠉⠀⠀⠀⠀⠀⠀⠀⢣⡘⣿⡰⡜⢦⢹⡆⠀⠀⢸⡏⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⡾⢀⣠⠞⠁⣰⠄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠸⣧⢻⡜⠆⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⣴⠃⠈⠀⢠⡴⠃⠀⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⣄⢹⡇⣷⡔⢖⠢⠴⣎⢿⣆⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠠⠚⠁⠀⢀⣴⠟⠀⠀⠀⠀⠀⠀⢐⣚⣿⡿⠿⠿⠿⣶⣼⣷⠸⣿⠋⢷⡀⠈⣦⢻⣆⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠋⠀⠀⠀⠀⠀⠠⠔⠋⠀⠀⠀⠀⠀⠀⢀⣴⠟⠋⠁⠀⠀⠀⠀⠈⣿⣿⠀⡇⠀⠀⠛⢆⠈⣏⢿⡆⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣄⣀⣰⡿⠉⢠⢴⠶⢶⣦⡀⠀⠀⣿⣿⠀⡇⢀⡴⣶⣾⡦⠉⠘⣿⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⡴⣫⠵⠚⠛⠓⠮⠟⣟⠁⠀⠈⠾⣷⡤⠽⣿⠀⠀⣿⡟⠀⢻⢸⡿⠟⠙⡆⠀⠀⢹⣇⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⡞⠈⠁⠀⠀⠀⠀⠀⠀⠀⠙⠶⣄⣀⡀⠉⠉⠁⢠⠾⠛⠃⠀⠈⠁⠀⡀⣸⠁⠀⠀⠈⣿⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡇⠀⠀⠀⠀⣿⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢄⡀⠀⠀⠀⠈⠳⣄⠀⠀⢰⠏⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⣄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣄⠀⠀⠀⠈⢷⣠⠏⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠈⠻⣳⣄⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⠟⠉⠙⢾⡇⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⢨⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⣦⡀⠘⢽⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠲⣄⢠⢿⣿⣆⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠸⣆⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢶⣄⡀⠈⠳⣤⡀⠀⠀⠀⠀⠀⠈⠳⣄⣁⣠⣿⡎⠘⣦⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⡄⠀⠘⢦⡘⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠒⠬⠿⠶⠤⣄⣀⣀⡤⠤⠤⠭⠟⠋⠀⠀⢻⣇ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠏⠀⠀⢰⡇⠀⠀⠀⠙⠲⣬⣛⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿ ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠈⠙⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠀⢸⠀⠘ ⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠋⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⠀⠀ ⠸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠹⣿⡄⠀⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢠⡟⠀⠀ ⠀⠈⠧⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠹⣿⣆⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⣼⢁⡾⠁⠀⠀ ⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠘⣿⡄       bozkurt⠀⠀⠀⠀⠀⠀  ⣸⠃⠀⠀⣰⠯⠋⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⠂⠈⣿⡄⠀⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠙⣇⠀⠈⣇⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠐⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⠀⠀⠸⠆⠀⢸⡀⠀⠚⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤ ⣤⣤⡤⠤⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⠁⣀⡁⠀⠉⣉⣋⡍⣁⣉⣉⣉⠋⡉⠉⢉⣱⠀⠀⠀       
                                                                                          
""")

banner()
show_options()

def get_mac():

  try:


    eth0_path = '/sys/class/net/eth0'
    if os.path.exists(eth0_path): #dizinin sistemde olup olup olmadığını kontrol ediyor exists modülü
        # eth0 dizini varsa, MAC adresini oku ve ekrana yazdır
        #eth0 arayüzü için mac adresi oku
        maceth0 = open('/sys/class/net/eth0/address').readline()
        if maceth0:
            print (COLOR.BRIGHT_BLUE + "[#] Your eth0  MACADDRESS is : ", maceth0 + COLOR.WHITE)
        else:
            print("[!] Unable to retrieve eth0 Mac address")



    wlan0_path = '/sys/class/net/wlan0'
    if os.path.exists(wlan0_path):
        #wlan0 arayüzü için mac adresi oku
        macwlan0 = open('/sys/class/net/wlan0/address').readline()
        if macwlan0:
            print (COLOR.BRIGHT_BLUE + "[#] Your wlan0  MACADDRESS is : ", macwlan0 + COLOR.WHITE)
        else:
            print("[!] Unable to retrieve eth0 Mac address")
            

  except: #mac adresi alınamazsa default mac atanır
    mac = "00:00:00:00:00:00"


def show_ip():
    try:

        url = 'https://api.ip.sb/geoip'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        getgeo = requests.get(url, headers=headers)
        getgeo_json=getgeo.json()


        getip = requests.get('https://api.ip.sb/ip',headers=headers)

        print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'IP      '.ljust(15),           ':' + COLOR.RED + getip.text)
        print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'COUNTRY ' .ljust(15),            ':' + COLOR.RED + getgeo_json['country'])

        if 'city' in getgeo_json:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'CITY    '  .ljust(15),       ':' + COLOR.RED + getgeo_json['city'])
        else:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'CITY    ' .ljust(15),        ':' + COLOR.WHITE + 'UNKNOWN')


        if 'organization' in getgeo_json:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'Organization '.ljust(15),   ':' + COLOR.RED + getgeo_json['organization'])
        else:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'Organization ' .ljust(15),   ':' + COLOR.WHITE + 'UNKNOWN')

        if 'timezone' in getgeo_json:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'Timezone    '  .ljust(15),  ':' + COLOR.RED + getgeo_json['timezone'])
        else:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'Timezone    '  .ljust(15),   ':' + COLOR.WHITE + 'UNKNOWN')



        if 'country_code' in getgeo_json:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'Country Code ' .ljust(15),  ':' + COLOR.RED + getgeo_json['country_code'])
        else:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'Country Code ' .ljust(15),    ':' + COLOR.RED + 'UNKNOWN')
        if 'region_code' in getgeo_json:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'Region Code ' .ljust(15),   ':' + COLOR.RED + getgeo_json['region_code'])
        else:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'Region Code ' .ljust(15),    ':' + COLOR.WHITE + 'UNKNOWN')

        if 'latitude' and 'longitude' in getgeo_json:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'Locate ' .ljust(15),   ':' + COLOR.RED + str(getgeo_json['latitude']) +','+str(getgeo_json['longitude']))
        else:
            print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'Region Code ' .ljust(15),    ':' + COLOR.WHITE + 'UNKNOWN')





    except Exception as e:
        print("An error occurred while fetching IP and geo information:", str(e))


def start_anonsurf():
    print(COLOR.LIGHT_GREEN + '\n[*] ' + COLOR.WHITE + 'Changing IP Address ..')
    os.system(' anonsurf start >/dev/null 2>&1')
    print(COLOR.LIGHT_GREEN + '[+] Changed Successfully!\n'+ COLOR.WHITE)

def change_ip_repeatedly():

    try:

        ip_change_delay = int(input(COLOR.YELLOW + '\n[?] ' + COLOR.WHITE + 'Change my IP Every '+COLOR.LIGHT_RED + '[SECONDS]' + COLOR.WHITE + ' : '))

        if(ip_change_delay == 0):

            print(COLOR.RED + '[-] Please Enter a Correct Number!' + COLOR.WHITE)
            sleep(2)
            os.system('clear')
            show_options()
            Engine()

        print(COLOR.LIGHT_GREEN + '[*] ' + COLOR.WHITE + 'Running IP Changer Service..')
        command_1 = f'anonsurf start >/dev/null 2>&1'
        os.system(command_1)

        print(COLOR.LIGHT_GREEN + '[+] Successfully Run!')
        print(COLOR.LIGHT_CYAN + '\n[*] ' + COLOR.WHITE + 'Changing IP Every' + COLOR.LIGHT_RED + ' {}S '.format(ip_change_delay) + '\n')
        print(COLOR.DARK_GRAY + '- - - - - - - - - - - - - - - - - -')

        test = ip_change_delay

        try:
            while test > 0:
                sleep(test)
                command_2 = f'anonsurf change  >/dev/null 2>&1'
                os.system(command_2)
                print(COLOR.RED+"IP is Changed")
                
                
                
                print(COLOR.DARK_GRAY + '- - - - - - - - - - - - - - - - - -')
                




        except KeyboardInterrupt:

            os.system('clear')
            show_options()
            Engine()

    except ValueError:
        print(COLOR.RED + '[-] Please Enter a Correct Number!' + COLOR.WHITE)
        sleep(2)
        os.system('clear')
        show_options()
        Engine()

def stop():
    os.system('anonsurf stop >/dev/null 2>&1')
    print(COLOR.LIGHT_GREEN + '\n[+] Successfully Stopped!\n'+ COLOR.WHITE)

def change_macaddress():
    print(COLOR.LIGHT_GREEN + '\n[*] ' + COLOR.WHITE + 'Running MACCHANGER Service..')
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('ifconfig eth0 down >/dev/null 2>&1')
        os.system('macchanger eth0 -r >/dev/null 2>&1')
        os.system('ifconfig eth0 up >/dev/null 2>&1')

    elif 'wlan0' in eth:
        os.system('ifconfig wlan0 down >/dev/null 2>&1')
        os.system('macchanger wlan0 -r >/dev/null 2>&1')
        os.system('ifconfig wlan0 up >/dev/null 2>&1')
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {} -r >/dev/null 2>&1'.format(interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def goodbye():
    print(COLOR.VIOLET + '\n[-] Thanks For Using Salvio Hexia!\n')
    exit()

def MAC():

    try:

        while True:

            choice = input(COLOR.GREEN + STYLE.ITALIC + '[Salvio Hexia]~[mac]' + COLOR.WHITE +  ' > ' + COLOR.WHITE)

            if(choice == '1'):
                print('\n')
                change_macaddress()
                get_mac()
            elif(choice == '2'):
                print('\n')
                macvendors.mac_samsung()
                get_mac()
            elif(choice == '3'):
                print('\n')
                macvendors.mac_apple()
                get_mac()
            elif(choice == '4'):
                print('\n')
                macvendors.mac_huawei()
                get_mac()
            elif(choice == '5'):
                print('\n')
                macvendors.mac_nokia()
                get_mac()
            elif(choice == '6'):
                print('\n')
                macvendors.mac_blackberry()
                get_mac()
            elif(choice == '7'):
                print('\n')
                macvendors.mac_motorola()
                get_mac()
            elif(choice == '8'):
                print('\n')
                macvendors.mac_htc()
                get_mac()
            elif(choice == '9'):
                print('\n')
                macvendors.mac_google()
                get_mac()
            elif(choice == '10'):
                print('\n')
                macvendors.macvendors.mac_asus()
                get_mac()
            elif(choice == '11'):
                print('\n')
                macvendors.mac_FUJITSU()
                get_mac()
            elif(choice == '12'):
                print('\n')
                macvendors.mac_toshiba()
                get_mac()
            elif(choice == '13'):
                print('\n')
                macvendors.mac_acer()
                get_mac()
            elif(choice == '14'):
                print('\n')
                macvendors.mac_dell()
                get_mac()
            elif(choice == '15'):

                print('\n')
                macvendors.mac_hp()
                get_mac()
            elif(choice == 's' or choice == 'S' or choice == 'mac' or choice == 'show mac'):
                print('')
                get_mac()
            elif(choice == 'b' or choice == 'B' or choice == 'back'):
                clear()
                Engine()
            elif(choice == 'X' or choice == 'x' or choice == 'exit' or choice == 'quit'):
                quit()
    except KeyboardInterrupt:
        print('\n')
        goodbye()


def clear():
    os.system('clear')
    show_options()

def Engine():

    try:

        while True:

            choice = input(COLOR.GREEN + STYLE.ITALIC + '[Salvio Hexia]' + COLOR.WHITE +  ' > ' + COLOR.WHITE)

            if(choice == '1' or choice.lower() == 'hide my ip once'):
                os.system('clear')
                show_options()
                start_anonsurf()
                
                

            elif(choice == '2' or choice.lower() == 'hide my ip repeatedly'):
                os.system('clear')
                show_options()
                change_ip_repeatedly()
                if(KeyboardInterrupt):
                    goodbye()

            elif(choice == '3' or choice.lower() == 'change ip'):
                os.system('clear')
                show_options()

                os.system('anonsurf start >/dev/null 2>&1')
                os.system('anonsurf change >/dev/null 2>&1')
                print(COLOR.LIGHT_GREEN + '\n[+] Successfully Changed!\n'+ COLOR.WHITE)
                show_ip()
                print('\n')

            elif(choice == '4' or choice.lower() == 'change my mac address'):
                os.system('clear')                
                show_mac_options()
                MAC()
            elif(choice == '5' or choice.lower() == 'do it all'):
                os.system('clear')
                show_options()
                start_anonsurf()
                os.system('anonsurf change >/dev/null 2>&1')
                show_ip()
                change_macaddress()
                get_mac()
            elif(choice == '6' or choice.lower() == 'show ip'):
                os.system('clear')
                show_options()
                print('\n')
                show_ip()
                print('\n')

            elif(choice == '7' or choice.lower() == 'stop'):
                os.system('clear')
                show_options()
                stop()

            elif(choice == '8' or choice.lower() == 'clear'):
                show_options()
                clear()

            elif(choice == '9'or choice.lower() == 'quit' or choice.lower() == 'exit'):
                os.system('clear')
                show_options()
                goodbye()

            elif(choice == '10' or choice.lower() == 'show ip_2'):
                os.system('clear')
                show_options()
                os.system('bash ip_show.sh')  

            elif(choice == '11' or choice.lower() == 'show ip_3'):
                os.system('clear')
                show_options()
                os.system('anonsurf myip 2>&1')

            else:
                print(COLOR.RED + '[-] Wrong Command!' + COLOR.WHITE)

    except KeyboardInterrupt:
        print('\n')
        goodbye()

Engine()

