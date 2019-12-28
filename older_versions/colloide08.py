#!/usr/bin/python
#
# MCD's Colloide v0.8
# Thessaloniki, GREECE 2017 - greekhacking.gr
# GNU General Public Lisence
# Pronounced: Kow Lawd
#
#     DO NOT USE FOR MALICIOUS PURPOSES! 
#                THE DEVELOPER HAS NO RESPONSIBLITY FOR ANY DAMAGE CAUSED!
#
#
#  				 _.:' VERSION DIARY ':._
#
# In version 0.1:
#	Program is working!
# In version 0.2:
#	Minor bugs fixed
#	Updated the links file
# In version 0.3:
#	Major bug fixed
#	Minor bugs fixed as well
#	Updated the links file
# 	Added option / argument parsing
#	Added legals
# In version 0.4:
#	Minor bugs fixed
#	General stracture has been updated
#	Wordlist option added - Only links.txt could be used before this update
#	Added ASCII logo
#	Added the sexy ASCII wolf
# In version 0.5 MAJOR RELEASE
#	Minor bugs fixed
#	Major bug fixed
#	Updated ASCII logo
#	Updated ASCII wolf
#	Program has been released to the masses!
# In version 0.6:
# 	Minor bugs fixed
# 	Option to save the pages into a txt page added
# 	Added some comments to help contributors read the code
# 	Added a function that checks whether the URL is valid or not
# In version 0.7:
#	One major bug fixed
#	Minor bugs fixed as well
# In version 0.8:
#	Added colors
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Project on GitHub:
#	http://yamechanic.com/C3vc
#   Website:
#	http://yamechanic.com/C41V
#
#   Report bugs: anivsante2@gmail.com
#   or /issues if you use github
# 
# # # # # # # # # # # # # # # # # # # # # # # #  

# MODULES / LIBRARIES:

from __future__ import print_function #because some print functions print quotation marks and commas
import sys 
import argparse
import os
import socket
from urllib2 import Request, urlopen, URLError, HTTPError
import colorama
from colorama import Fore, Back, Style

# CODE:

def banner(): #banner with logo - patorjk.com
	print("MCD's")
	print("_________        .__  .__         .__    .___     ")
	print("\_   ___ \  ____ |  | |  |   ____ |__| __| _/____  ")
	print("/    \  \/ /  _ \|  | |  |  /  _ \|  |/ __ |/ __ \ ")
	print("\     \___(  <_> )  |_|  |_(  <_> )  / /_/ \  ___/")
	print(" \______  /\____/|____/____/\____/|__\____ |\___  >")
	print("        \/                                \/    \/ ")
	print("MCD's")
	print("Colloide v 0.8")
	print("MD 2017")
	print("www.greekhacking.gr\n\n")
def opts():
	print("    -h --help     Display the help panel (Shown right now)")
	print("    -u --URL      The URL to the website")
	print("    -p --pages    Path to the wordlist with the page names / links")
	print("    -l --legals   License & legal disclaimer")
	print("    -s --save     Save pages on a text file (name of the file)")
	print("    -L --limit    Add limit to the pages (Integer)")
	print("    -v --verbose  Show all attempts\n\n")
def legals():
	#License
	print("MCD's Colloide version 0.8 is free software. It can be re-distributed ")
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
		print(Fore.RED + Style.BRIGHT + "[-] Invalid path to the wordlist. File could not be found.\n" + Style.RESET_ALL)
	 
def findAdmin():
	if txt:
		#print("Please type the name of the text file to save the pages to.")
		#print("example: pages.txt")          COMMENTED CODE
		#tfilename = raw_input(">> ")       WONT BE USED - YOU CAN REMOVE IT
		tfilename = txt
		f = open(str(tfilename) ,'w+')
		f.write("Thessaloniki, Greece 2017\n")
		f.write("greekhacking.gr\n")
		print("\n")
	print(Fore.RED + Style.BRIGHT + "[!] Report bugs: anivsante2@gmail.com \n" + Style.RESET_ALL) 
					#OR https://github.com/MichaelDim02/colloide.py/issues
	print(Fore.RED + Style.BRIGHT + "[!] Press Ctrl + C to terminate the process.\n" + Style.RESET_ALL)
	try:	
		IP = socket.gethostbyname(URL)
		print(Fore.RED + Style.BRIGHT + "[!] Attacking host: ", IP, " - ", URL, "\n" + Style.RESET_ALL)
		if txt:
			f.write("Attacking:\n")
			f.write("\n")
			f.write(str(URL))
			f.write("\n")
			f.write(str(IP))
			f.write("\n")
	except socket.gaierror:
		print(Fore.RED + Style.BRIGHT + "[!] Invalid URL address. Connection could not be established;\n" + Style.RESET_ALL)
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
			if ver:
				notworking = "[ATTEMPT] - " + req_link
				#notworking.rstrip() So it does not print lines between attempt output line
			#identifies links that show up HTTP error
			try:
				response = urlopen(req)
			except HTTPError as e:
				if ver:
					print(Fore.GREEN + notworking.rstrip() + Style.RESET_ALL) 
				continue
			except URLError as e:
				if ver:
					print(Fore.GREEN + notworking.rstrip() + Style.RESET_ALL)
				continue 
			else: #prints working link
				if ver != True:
					print("[+] Link Found -> " + req_link + "") 
					# if verbose if off 
				if ver:
					print("\n[+] Link Found -> " + req_link + "") 
					#because in verbose mode failed attempts don't have \n at the end
				found = found + 1
				if txt:
					f = open(str(tfilename) ,'a')
					f.write(req_link + "\n")
				else:
					pass
		except KeyboardInterrupt:
			print(Fore.RED + Style.BRIGHT + "\n[!] Process has been terminated - Ctrl + C has been pressed.\n" + Style.RESET_ALL)
			if txt:
				print("All working pages have been saved at: ", tfilename, "\n")	
			sys.exit(0)
	if found > int(limit):
		print(Fore.RED + Style.BRIGHT + "[!] Process has been terminated due to the limitation that has been set\n" + Style.RESET_ALL)
	if txt:
		print("All working pages have been saved at: ", tfilename, "\n")

#Argument parsing 
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--URL", help="The URL to the website")
parser.add_argument("-p", "--pages", help="Path to the wordlist with the page names / links") 
parser.add_argument("-l", "--legals", action='store_true', help="License & legal disclaimer")
parser.add_argument("-s", "--save", help="Save all working pages on a text file")
parser.add_argument("-L", "--limit", help="Add limit to the pages. Integer", default="10")
parser.add_argument("-v", "--verbose", help="Show all attempts", action="store_true")

#Declaring Argument Variables
args = parser.parse_args()
links = args.pages
URL = args.URL
txt = args.save
limit = args.limit
ver = args.verbose

if args.URL and args.pages:
	check_names(links)
elif args.legals:
	banner()
	legals()
else:
	banner()
	opts()
print("Usage: python colloide.py -u [URL] -p [WORDLIST] -s [TEXT FILE] -L [NUMBER]")

#
#   MCD's
#   Colloide v0.8
#   Can be modified 
#   Can be distributed commercially
#   Can be distributed non-commercially 
#   Under the terms of the GNU general public license (2007)
#   Project on GitHub:
#	http://yamechanic.com/C3vc
#   Website:
#	http://yamechanic.com/C41V
#
# # # # # # # # # # # # # # # # # # # # # # # # #
