# Colloide v0.6
# Thessaloniki, GREECE 2017 - greekhacking.gr 
# Michael Constantine Dimopoulos
# GNU General Public Lisence
# Pronounced: Kow Lawd
# In this version (0.6):
# Minor bugs fixed
# Option to save the pages into a txt page added
# Added some comments to help contributors read the code
# Added a function that checks whether the URL is valid or not
# https://github.com/MichaelDim02/colloide
# Report bugs: anivsante2@gmail.com 
# or /issues if you use github
# # # # # # # # # # # # # # # # # # 

#CODE:

from __future__ import print_function #because some print functions print quotation marks and commas
import sys 
import argparse
import os
import socket
from urllib2 import Request, urlopen, URLError, HTTPError

def banner(): #banner with logo - patorjk.com 
	print("_________        .__  .__         .__    .___     ")
	print("\_   ___ \  ____ |  | |  |   ____ |__| __| _/____  ")
	print("/    \  \/ /  _ \|  | |  |  /  _ \|  |/ __ |/ __ \ ")
	print("\     \___(  <_> )  |_|  |_(  <_> )  / /_/ \  ___/")
	print(" \______  /\____/|____/____/\____/|__\____ |\___  >")
	print("        \/                                \/    \/ ")
	print("Colloide v 0.6")
	print("Michael C. Dimopoulos 2017")
	print("www.greekhacking.gr\n\n")
def opts():
	print("    -h  --help   Display the help panel (Shown right now)")
	print("    -u --URL     The URL to the website")
	print("    -p --pages   Path to the wordlist with the page names / links")
	print("    -l --legals  License & legal disclaimer")
	print("    -s --save    Save pages on a text file (name of the file will be asked lat)")
	print("    -L --limit   Add limit to the pages (Integer)\n\n")
def legals():
	#License
	print("Colloide version 0.6 is free software. It can be re-distributed ")
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
		print("[-] Invalid path to the wordlis. File could not be found.\n")
	 
def findAdmin():
	if txt:
		#print("Please type the name of the text file to save the pages to.")
		#print("example: pages.txt")          COMMENTED CODE
		#tfilename = raw_input(">> ")       WONT BE USED - YOU CAN REMOVE IT
		tfilename = txt
		f = open(str(tfilename) ,'w+')
		f.write("Colloide v0.6\n")
		f.write("Michel Constantine Dimopoulos\n")
		f.write("Thessaloniki, Greece 2017\n")
		f.write("greekhacking.gr\n")
		print("\n")
	print("[!] Report bugs: anivsante2@gmail.com \n") #OR https://github.com/MichaelDim02/colloide.py/issues
	print("[!] Press Ctrl + C to terminate the process.\n")
	try:	
		IP = socket.gethostbyname(URL)
		print("[!] Attacking host: ", IP, " - ", URL, "\n")
		if txt:
			f.write("Attacking:\n")
			f.write("\n")
			f.write(str(URL))
			f.write("\n")
			f.write(str(IP))
			f.write("\n")
	except socket.gaierror:
		print("[!] Invalid URL address. Connection could not be established;\n")
		sys.exit(0)
	fi = open(links,"r");
	found = 0
	while (found <= int(limit)): 
		try:
			sub_link = fi.readline() #Page name
			if not sub_link:
				break
			link = URL #website name
			req_link = "http://"+link+"/"+sub_link #Final link for attempt
			req = Request(req_link)
			#identifies links that show up HTTP error
			try:
				response = urlopen(req)
			except HTTPError as e:
				continue
			except URLError as e:
				continue 
			else: #prints working link
				print("[+] Link Found -> " + req_link)
				found = found + 1
				if txt:
					f = open(str(tfilename) ,'a')
					f.write(req_link + "\n")
				else:
					pass
		except KeyboardInterrupt:
			print("\n[!] Process has been terminated - Ctrl + C has been pressed.\n")
			print("All working pages have been saved at: ", tfilename, "\n")	
			sys.exit(0)
	if attempts > int(limit):
		print("[!] Process has been terminated due to the limitation that has been set\n")
	print("All working pages have been saved at: ", tfilename, "\n")

#Argument parsing 
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--URL", help="The URL to the website")
parser.add_argument("-p", "--pages", help="Path to the wordlist with the page names / links") 
parser.add_argument("-l", "--legals", action='store_true', help="License & legal disclaimer")
parser.add_argument("-s", "--save", help="Save all working pages on a text file")
parser.add_argument("-L", "--limit", help="Add limit to the pages. Integer", default="10")
#Declaring Argument Variables
args = parser.parse_args()
links = args.pages
URL = args.URL
txt = args.save
limit = args.limit

if args.URL and args.pages:
	check_names(links)
elif args.legals:
	banner()
	legals()
else:
	banner()
	opts()
print("Usage: python colloide.py -u [URL] -p [WORDLIST]")

#Can be modified 
#Can be distributed commercially
#Can be distributed non-commercially 
#Under the terms of the GNU general public license (2007)
#Michael Constantine Dimopoulos
#https://github.com/MichaelDim02/colloide
