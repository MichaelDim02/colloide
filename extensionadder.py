print("     .: MCDs COLLOIDE EXCLUSIVE :.")
print("Extension adding tool for file wordlists\n")
print("This tool is used to add filename extensions to a wordlist / dictionary.")
print("Just type the wordlist name and then the file extension you want to add")
print("Made by Michael Constantine Dimopoulos 2018 - anivsante2@gmail.com")
file_name = raw_input("Wordlist name: ")
xtension = raw_input("Extension: ")
if xtension.startswith("."):
	print("Dot /'./' found\n")
else:
	print("Dot /'./' not found - One will be added\n")
	xtension = "." + xtension
with open(file_name, 'r') as f:
    file_lines = [''.join([x.strip(), xtension, '\n']) for x in f.readlines()]

with open(file_name, 'w') as f:
    f.writelines(file_lines)
