# Colloide v0.5
# Thessaloniki, GREECE 2017 - greekhacking.gr
# Michael Constantine Dimopoulos
# GNU General Public Lisence
import sys
import argparse
import os
import socks
import socket
try: # For Python 3.0 and later
	from urllib.request import Request, urlopen
	from urllib.error import URLError, HTTPError
except ImportError: # Fall back to Python 2's urllib2
	from urllib2 import Request, urlopen, URLError, HTTPError

# STEM module for signaling tor network service
from stem import Signal
from stem.control import Controller

DEBUG_OUTPUT_DIR = "output/"

TOR_DEFAULT_CONTROLLER_PROXY_PORT = 9051
TOR_DEFAULT_PROXY_IP = "127.0.0.1"
TOR_DEFAULT_PROXY_PORT = 9050

controller = Controller.from_port(port = TOR_DEFAULT_CONTROLLER_PROXY_PORT)

def banner():
	print("_________        .__  .__         .__    .___     ")
	print("\_   ___ \  ____ |  | |  |   ____ |__| __| _/____  ")
	print("/    \  \/ /  _ \|  | |  |  /  _ \|  |/ __ |/ __ \ ")
	print("\     \___(  <_> )  |_|  |_(  <_> )  / /_/ \  ___/")
	print(" \______  /\____/|____/____/\____/|__\____ |\___  >")
	print("        \/                                \/    \/ ")
	print("Colloide v 0.5")
	print("Michael C. Dimopoulos 2017\n\n")
def opts():
	print("    -h  --help       Display the help panel (Shown right now)")
	print("    -u, --URL        The URL to the website")
	print("    -p, --pages      Path to the wordlist with the page names / links")
	print("    -l, --legals     License & legal disclaimer")
	print("    -t, --torenable  Enable tor proxy switching (!!! REQUIRES CONTROLLER PORT OPEN !!!)\n\n")
def legals():
	#License
	print("Colloide version 0.5 is free software. It can be re-distributed ")
	print("and / or modified under the terms of the GNU General Public License")
	print("as published by the Free Software Foundation; For more information")
	print("read the GNU General Public License that comes")
	print("along with this program.\n\n")
	#Disclaimer
	print("[!] Legal Disclaimer [!]")
	print("Information distributed by this tool may be used maliciously.")
	print("The developer has no responsibility for any damage caused by")
	print("this script or any unauthorized use of it.\n")
def wolf():
	#prints the ASCII colloide wolf
	print(" ___________________      ,     ,")
	print("[ COLLOIDE MISSION! ]     |\---/|       __--__")
	print("                         /      [     ,:',.  (`. ")
	print("                    __.-'|      /    |  `'_.   .|")
	print("           __ ___.-'         \__)   |   _ : () _ |")
	print("        .-'  '        :   :  _/      |    .  .  |")
	print("       / ,    .        .   _ |        ':_)  ,_|'")
	print("      :  ;    :        :   _/             --   ")
	print("      |  |   .'     __:   /      ")
	print("      |  :   /'----'| \  |              __________")
	print("      \  |\  |      | /| |_______,-----'")
	print("       '.'| /__,----| \ | ")
	print("_______| /|.'       '.l \\\_")
	print("       || ||             '-'")
	print("       '-''-'\n")
def check_names(infile, torEnabled=0):
	if os.path.exists(infile):
		banner()
		wolf()
		findAdmin(torEnabled)
	else:
		banner()
		opts()
		print("Invalid path to the wordlis. File could not be found.")

def findAdmin(torEnabled=0):
	f = open(links,"r");
	print("[!] Report bugs: anivsante2@gmail.com \n") # https://github.com/MichaelDim02/colloide/issues instead?

	if torEnabled:
		print("You have enabled Tor proxy passthrough. Please be aware that this might significantly slow down the scan.")
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, TOR_DEFAULT_PROXY_IP, TOR_DEFAULT_PROXY_PORT)
		socket.socket = socks.socksocket

	while True:
		generateNewTorIP()
		sub_link = f.readline()
		if not sub_link:
			break
		link = URL
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			log(link, req_link)
			print("[+] Link Found -> ",req_link)

def generateNewTorIP(password="el_passwordo", controllerPort=TOR_DEFAULT_CONTROLLER_PROXY_PORT):
	controller.authenticate(password=password)
	controller.signal(Signal.NEWNYM)

def log(name, data):
	if not os.path.exists(DEBUG_OUTPUT_DIR):
		os.makedirs(DEBUG_OUTPUT_DIR)
	logFile = open(DEBUG_OUTPUT_DIR + name.replace("/", ""), "a")
	logFile.write(data)

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--URL", help="The URL to the website")
parser.add_argument("-p", "--pages", help="Path to the wordlist with the page names / links")
parser.add_argument("-l", "--legals", action='store_true', help="License & legal disclaimer")
parser.add_argument("-t", "--torenable", help="Enable proxying through TOR to 'anonymize' traffic (requires TOR to be running and controller configured (default port 9051)) !!! WILL INCREASE RUN TIME DRAMATICALLY !!!")
args = parser.parse_args()
links = args.pages
URL = args.URL
torIsEnabled = args.torenable
if args.URL and args.pages:
	check_names(links, torEnabled=args.torenable)
elif args.legals:
	banner()
	legals()
else:
	banner()
	opts()
	print("Usage: python colloide.py -u [URL] -p [WORDLIST]")
