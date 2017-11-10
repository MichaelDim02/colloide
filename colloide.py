# Colloide v0.5
# Thessaloniki, GREECE 2017 - greekhacking.gr 
# Michael Constantine Dimopoulos
# GNU General Public Lisence
# Pronounced: Kow Lowd
import sys 
import argparse
import os
from urllib2 import Request, urlopen, URLError, HTTPError

def banner(): #banner with logo - patorjk.com 
	print("_________        .__  .__         .__    .___     ")
	print("\_   ___ \  ____ |  | |  |   ____ |__| __| _/____  ")
	print("/    \  \/ /  _ \|  | |  |  /  _ \|  |/ __ |/ __ \ ")
	print("\     \___(  <_> )  |_|  |_(  <_> )  / /_/ \  ___/")
	print(" \______  /\____/|____/____/\____/|__\____ |\___  >")
	print("        \/                                \/    \/ ")
	print("Colloide v 0.5")
	print("Michael C. Dimopoulos 2017\n\n")
def opts():
	print("    -h  --help   Display the help panel (Shown right now)")
	print("    -u, --URL    The URL to the website")
	print("    -p, --pages  Path to the wordlist with the page names / links")
	print("    -l, --legals License & legal disclaimer\n\n")
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
def check_names(infile):    #Checking the path to the wordlist
	if os.path.exists(infile):
		banner()    #calls the banner function
		wolf()      #calls the sexy ASCII wolf wallpaper
		findAdmin() #calls the function that basically does the job 
	else: #in case wordlist cant be found
		banner()
		opts()
		print("Invalid path to the wordlis. File could not be found.")
	 
def findAdmin():
	f = open(links,"r");
	print("[!] Report bugs: anivsante2@gmail.com \n") #OR https://github.com/MichaelDim02/colloide.py/issues
	while True:
		sub_link = f.readline() #Page name
		if not sub_link:
			break
		link = URL #website name
		req_link = "http://"+link+"/"+sub_link #Final link for attempt
		req = Request(req_link)
		try:
			response = urlopen(req)
			#identifies links that show up HTTP error
		except HTTPError as e:
			continue
		except URLError as e:
			continue 
		else: #prints working link
			print "[+] Link Found -> " + req_link


#Argument parsing 
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--URL", help="The URL to the website")
parser.add_argument("-p", "--pages", help="Path to the wordlist with the page names / links") 
parser.add_argument("-l", "--legals", action='store_true', help="License & legal disclaimer")
args = parser.parse_args()
links = args.pages
URL = args.URL
if args.URL and args.pages:
	check_names(links)
elif args.legals:
	banner()
	legals()
else:
	banner()
	opts()
	print("Usage: python colloide.py -u [URL] -p [WORDLIST]")
