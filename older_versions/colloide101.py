#!/usr/bin/python
#
# MCD's Colloide v1.0.1
# Thessaloniki, GREECE 2017 - greekhacking.gr
# Michael Constantine Dimopoulos
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
# In version 0.8.5
#	Added status code next to links
#	Added more link wordlists, more specific to each language
# In version 0.9:
#	Added status code method
# In version 0.9.5
#	Quick robots.txt check added
# In version 1.0.0
#	Directory option added (-f) to search inside of a particular dir
#	Fixed major bug in the status method (false status code retrieved)
#	Removed status code from the urlerror method
#       Red when unauthorized or forbidden in the status method
# In version 1.0.1
#	Users are able to disable/enable ascii by typing -a
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
#SYSTEM MODULES#
import sys
import os
import argparse
#NETWORK MODULES#
import httplib
import socket
import urllib2
import requests
from urllib2 import Request, urlopen, URLError, HTTPError
#STYLE MODULES#
import colorama
from colorama import Fore, Back, Style

# CODE:

def logo(): #logo - patorjk.com
	print("MCD's")
	print("_________        .__  .__         .__    .___     ")
	print("\_   ___ \  ____ |  | |  |   ____ |__| __| _/____  ")
	print("/    \  \/ /  _ \|  | |  |  /  _ \|  |/ __ |/ __ \ ")
	print("\     \___(  <_> )  |_|  |_(  <_> )  / /_/ \  ___/")
	print(" \______  /\____/|____/____/\____/|__\____ |\___  >")
	print("        \/                                \/    \/ ")
def checkasciilogo():
	check_value = open("ascii_disable_option_value.txt","r")
	checkvalue = check_value.read(1)
	if checkvalue == "0":
		logo()
	check_value.close()
def banner(): #banner with logo - patorjk.com
	checkasciilogo()
	print("MCD's")
	print("Colloide v 1.0.1")
	print("Michael C. Dimopoulos 2017")
	print("www.greekhacking.gr\n\n")
def opts():
	print("  --robots        Check for robots.txt file")
	print("    -u --URL      The URL to the website")
	print("    -c --content  Display contents of robots.txt")
	print("    -d --dump     Dump the contents to a text file\n")
	print("  --status        Use the HTTP status code method (Faster)")
	print("  --urlerror      Use the HTTP/URL error method (More reliable)")
	print("    -h --help     Display the help panel (Shown right now)")
	print("    -u --URL      The URL to the website")
	print("    -f --folder   Directory to search in")
	print("    -p --pages    Path to the wordlist with the page names / links")
	print("    -l --legals   License & legal disclaimer")
	print("    -s --save     Save pages on a text file (name of the file)")
	print("    -L --limit    Add limit to the pages (Integer)")
	print("    -v --verbose  Show all attempts\n")
	print("    -a --ascii    Enable/Disable ASCII\n\n")
def legals():
	#License
	print("MCD's Colloide version 1.0.1 is free software. It can be re-distributed ")
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
def checkasciiwolf():
	check_value = open("ascii_disable_option_value.txt","r")
	checkvalue = check_value.read(1)
	if checkvalue == "0":
		wolf()
	else:
		print(" ___________________ ")
		print("[ COLLOIDE MISSION! ]\n\n")
	check_value.close()
def robots_check():
	print("MCD's Colloide v1.0.0")
	print("Report bugs: /MichaelDim02/colloide.py/issues")
	print("Robots.txt check function\n")
	print("INFO:")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("URL           =       ", URL)
	robots_link = "http://"+URL+"/robots.txt"
	robots_value = False #robots_value - if it has been found or not
	try:
		IP = socket.gethostbyname(URL)
		print("IP            =       ", IP)
		robot = urllib2.urlopen(robots_link)
		print("robots        =        True")
		robots_value = True
		#robots_value - if it has been found or not

	#if it encouters url error or httperror / exception robots.txt doesn't exist and it prints false
	#WARNING: This could also mean the given URL is not correct
	#so it is prevented like so:
	except socket.gaierror:
		print("[!] Incorrect URL address")
	except URLError as e:
		print("robots        =        False")
		robots_value = False
	except HTTPError as e:
		print("robots        =        False")
		robots_value = False
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
	if robots_value == True:
		contentspage = robot.read()
		#the content that will be dumped / displayed
		if content:
			print("CONTENT:")
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
			print(contentspage)
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		if dump:
			dump_name = "robots_%s.txt" % URL
			rf = open(dump_name, "w+")
			rf.write(str(contentspage))
			rf.close()
			print("\nCONTENT DUMPED AT: ", dump_name)

def scan_start():
	print(Fore.RED + Style.BRIGHT + "[!] Report bugs: /MichaelDim02/colloide.py/issues \n" + Style.RESET_ALL)

	print(Fore.RED + Style.BRIGHT + "[!] Press Ctrl + C to terminate the process.\n" + Style.RESET_ALL)

def check_names(infile):    #Checking the path to the wordlist
	if os.path.exists(infile):
		if status_method:
			banner()    #calls the banner function
			checkasciiwolf()      #calls the sexy ASCII wolf wallpaper
			statusfindAdmin() #calls the function that basically does the job
		elif error_method:
			banner()
			checkasciiwolf()
			findAdmin()
	else: #in case wordlist cant be found
		banner()
		opts()
		print(Fore.RED + Style.BRIGHT + "[-] Invalid path to the wordlist. File could not be found.\n" + Style.RESET_ALL)
# THIS IS THE STATUS CODE METHOD
def statusfindAdmin():
	if txt:
		tfilename = txt
		f = open(str(tfilename) ,'w+')
		f.write("MCD's Colloide v1.0.1\n")
		f.write("Michel C. Dim.\n")
		f.write("Thessaloniki, Greece 2017\n")
		f.write("greekhacking.gr\n")
		print("\n")
	scan_start()
	try:
		IP = socket.gethostbyname(URL)
		print(Fore.RED + Style.BRIGHT + "[!] Attacking host: ", IP, " - ", URL, "\n" + Style.RESET_ALL)
		if txt:
			f.write("Attacking:\n")
			f.write("\n")
			f.write(str(URL))
			f.write("\n")
			f.write(str(IP))
			f.write("\n\n")
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
			if directory:
				req_link = "http://"+link+directory+sub_link
			req = Request(req_link)
			con_link = link + "/" + sub_link
			con_ = requests.head(req_link)
			int_status_code_ = con_.status_code
			status_code_ = str(int_status_code_)
			notworking = "[ATTEMPT] - "+ status_code_ + " - " + req_link
			unauth = "[ANAUTHORIZED] - "+ status_code_+ " - " + req_link
			forbid = "[FORBIDDEN] - " + status_code_ + " - " + req_link
			if status_code_.startswith("4"):
				if ver:
					if int_status_code_ == 401:
						print(Fore.RED + unauth.rstrip() + Style.RESET_ALL)
					elif int_status_code_ == 403:
						print(Fore.RED + forbid.rstrip() + Style.RESET_ALL)
					else:
						print(Fore.GREEN + notworking.rstrip() + Style.RESET_ALL)
					#notworking.rstrip() So it does not print lines between attempt output line
					#identifies links that show up HTTP error
			else:
				if ver != True:
					print("[+] Link Found" + " - " + status_code_ +" -"+ " -> " + req_link + "")
					# if verbose if off
				if ver:
					print("\n[+] Link Found" + " - " + status_code_ +" -"+ " -> " + req_link + "")
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
		f.close()
# THIS IS THE HTTP/URL ERROR METHOD
def findAdmin():
	if txt:
		tfilename = txt
		f = open(str(tfilename) ,'w+')
		f.write("MCD's Colloide v1.0.1\n")
		f.write("Michael C. Dim.\n")
		f.write("Thessaloniki, Greece 2017\n")
		f.write("greekhacking.gr\n")
		print("\n")
	scan_start()
	try:
		IP = socket.gethostbyname(URL)
		print(Fore.RED + Style.BRIGHT + "[!] Attacking host: ", IP, " - ", URL, "\n" + Style.RESET_ALL)
		if txt:
			f.write("Attacking:\n")
			f.write("\n")
			f.write(str(URL))
			f.write("\n")
			f.write(str(IP))
			f.write("\n\n")
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
			if directory:
				req_link = "http://"+link+directory+sub_link
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
					print("[+] Link Found" + " -> " + req_link + "")
					# if verbose if off
				if ver:
					print("\n[+] Link Found" + " -> " + req_link + "")
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

def change_ascii():
	ascii_file = open("ascii_disable_option_value.txt", "r")
	checkascii = ascii_file.read(1)
	ascii_file.close()
	changeascii = open("ascii_disable_option_value.txt", "w")
	if checkascii == "1":
		changeascii.write("0")
		print("[+] ASCII enabled")
	elif checkascii == "0":
		changeascii.write("1")
		print("[+] ASCII disabled")

#Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("--robots", action="store_true", help="Check for robots.txt file")
parser.add_argument("-d", "--dump", action="store_true", help="Dump the contents to a text file")
parser.add_argument("-c", "--content", action="store_true", help="Display the contents of robots.txt")
#robots exclusive
parser.add_argument("--status", action="store_true", help="Use the HTTP status code method")
parser.add_argument("--urlerror", action="store_true", help="Use the HTTP/URL error method")
parser.add_argument("-u", "--URL", help="The URL to the website")
parser.add_argument("-f", "--folder", help="Directory to search in (must end and start with '/')")
parser.add_argument("-p", "--pages", help="Path to the wordlist with the page names / links")
parser.add_argument("-l", "--legals", action='store_true', help="License & legal disclaimer")
parser.add_argument("-s", "--save", help="Save all working pages on a text file")
parser.add_argument("-L", "--limit", help="Add limit to the pages. Integer", default="10")
parser.add_argument("-v", "--verbose", help="Show all attempts", action="store_true")
parser.add_argument("-a", "--ascii", help="Enable/Disable ASCII", action="store_true")

#Declaring Argument Variables
args = parser.parse_args()
status_method = args.status
error_method = args.urlerror
links = args.pages
URL = args.URL
directory = args.folder
txt = args.save
limit = args.limit
ver = args.verbose
ascii = args.ascii
#robots exclusive options / arguments
robots = args.robots
dump = args.dump
content = args.content

if error_method:
	status_method = False
	robots = False
elif error_method == False:
	status_method = True
	robots = False
elif error_method == False and status_method == False:
	robots = True

if args.URL and args.pages:
	check_names(links)
elif args.robots and args.URL:
	robots_check()
elif args.legals:
	banner()
	legals()
elif args.ascii:
	change_ascii()
else:
	banner()
	opts()
print("Usage:  python colloide100.py --[method] -u [URL] -p [WORDLIST] -s [TEXT FILE] -L [NUMBER] -v")
print("Robots: python colloide100.py --robots -u [URL] -d -c")

#
#   MCD's
#   Colloide v1.0.1
#   Can be modified
#   Can be distributed commercially
#   Can be distributed non-commercially
#   Under the terms of the GNU general public license (2007)
#   Michael Constantine Dimopoulos
#   Project on GitHub:
#	http://yamechanic.com/C3vc
#   Website:
#	http://yamechanic.com/C41V
#
# # # # # # # # # # # # # # # # # # # # # # # # #
