#!/usr/bin/python
#
# MCD's Colloide v0.9.5
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
import httplib
import os
import socket
import urllib2
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
	print("Colloide v 0.9.5")
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
	print("    -p --pages    Path to the wordlist with the page names / links")
	print("    -l --legals   License & legal disclaimer")
	print("    -s --save     Save pages on a text file (name of the file)")
	print("    -L --limit    Add limit to the pages (Integer)")
	print("    -v --verbose  Show all attempts\n\n")
def legals():
	#License
	print("MCD's Colloide version 0.9.5 is free software. It can be re-distributed ")
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
def robots_check():
	print("MCD's Colloide v0.9.5")
	print("Report bugs: anivsante2@gmail.com")
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
	print(Fore.RED + Style.BRIGHT + "[!] Report bugs: anivsante2@gmail.com \n" + Style.RESET_ALL) 
					#OR https://github.com/MichaelDim02/colloide.py/issues
	print(Fore.RED + Style.BRIGHT + "[!] Press Ctrl + C to terminate the process.\n" + Style.RESET_ALL)

def check_names(infile):    #Checking the path to the wordlist
	if os.path.exists(infile):
		if status_method:
			banner()    #calls the banner function
			wolf()      #calls the sexy ASCII wolf wallpaper
			statusfindAdmin() #calls the function that basically does the job
		elif error_method:
			banner()  
			wolf()
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
		f.write("MCD's Colloide v0.9.5\n")
		f.write("Michel Constantine Dimopoulos\n")
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
			con_ = httplib.HTTPConnection(str(URL))
			sub_link = fi.readline() #Page name
			if not sub_link:
				break
			link = URL #website name
			req_link = "http://"+link+"/"+sub_link #Final link for attempt
			req = Request(req_link)
			con_link = link + "/" + sub_link
			con_.request("GET", "/" + str(sub_link))
			int_status_code_ = con_.getresponse().status
			status_code_ = str(int_status_code_)
			if ver:
				notworking = "[ATTEMPT] - "+ status_code_ + " - " + req_link
				#notworking.rstrip() So it does not print lines between attempt output line
				#identifies links that show up HTTP error
				if status_code_.startswith("4"):
					print(Fore.GREEN + notworking.rstrip() + Style.RESET_ALL)
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
		f.write("MCD's Colloide v0.9.5\n")
		f.write("Michel Constantine Dimopoulos\n")
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
			con_ = httplib.HTTPConnection(str(URL))
			sub_link = fi.readline() #Page name
			if not sub_link:
				break
			link = URL #website name
			req_link = "http://"+link+"/"+sub_link #Final link for attempt
			req = Request(req_link)
			con_link = link + "/" + sub_link
			con_.request("GET", "/" + str(sub_link))
			int_status_code_ = con_.getresponse().status
			status_code_ = str(int_status_code_)
			if ver:
				notworking = "[ATTEMPT] - "+ status_code_ + " - " + req_link
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

#Argument parsing
parser = argparse.ArgumentParser() 
parser.add_argument("--robots", action="store_true", help="Check for robots.txt file")
parser.add_argument("-d", "--dump", action="store_true", help="Dump the contents to a text file")
parser.add_argument("-c", "--content", action="store_true", help="Display the contents of robots.txt")
#robots exclusive
parser.add_argument("--status", action="store_true", help="Use the HTTP status code method")
parser.add_argument("--urlerror", action="store_true", help="Use the HTTP/URL error method")
parser.add_argument("-u", "--URL", help="The URL to the website")
parser.add_argument("-p", "--pages", help="Path to the wordlist with the page names / links") 
parser.add_argument("-l", "--legals", action='store_true', help="License & legal disclaimer")
parser.add_argument("-s", "--save", help="Save all working pages on a text file")
parser.add_argument("-L", "--limit", help="Add limit to the pages. Integer", default="10")
parser.add_argument("-v", "--verbose", help="Show all attempts", action="store_true")

#Declaring Argument Variables
args = parser.parse_args()
status_method = args.status
error_method = args.urlerror
links = args.pages
URL = args.URL
txt = args.save
limit = args.limit
ver = args.verbose
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
else:
	banner()
	opts()
print("Usage:  python colloide095.py --[method] -u [URL] -p [WORDLIST] -s [TEXT FILE] -L [NUMBER] -v")
print("Robots: ptyhon colloide095.py --robots -u [URL] -d -c")

#
#   MCD's
#   Colloide v0.9.5
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
