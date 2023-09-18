import random
import time
import os

option = 0
while (option < 1 or option > 3):
	print("--- Welcome to Password Generator ---\n")
	print("\n--- Menu --- \n")
	option = int(input("Select option:\n -1) Show database\n -2) Generate new password\n -3) Quit\n:::"))


if (option == 1):
	print("----------------------------\n Information acquired: \n----------------------------\n")
	with open ("pwIndex.txt", 'r') as printFile:
		print(printFile.read())
	os.system("pause")


elif (option == 2):
	pwchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*().'

	length = int(input('Inform the lenght of the desired password:'))

	domain = input("Inform the domain for the created password:")

	username = ""

	selection1 = int(input("Wish to inform username aswell type 0 for No & 1 for Yes:"))
	if(selection1 == 1):
		username = input("Inform your username:")

	password = ""

	selection2 = int(input("Would you like a specific word in the password type 0 for No & 1 for Yes:"))
	if(selection2 == 1):
		password = input("Inform the desired word:")

	newLength = length - len(password)

	for pwd in range(length):
		print("...")
		time.sleep(0.5)
		password += random.choice(pwchars)
	pwFile = open ("pwIndex.txt", "a")

	pwFile.write("\n-------------------------------------------------\n")
	pwFile.write("Service: " + domain)
	if(username != ""):
		pwFile.write("\nUser: " + username)

	pwFile.write("\nPassword: " + password)

	print("Password generated!")
	print("Information added:\n ")
	print("Service:\n ", domain)
	if(username != ""):
		print("User:\n ", username)
	print("Password:\n ", password)

	pwFile.close()
	print("Ending program...")
	time.sleep(1)

	os.system('pause')	


else:
	print("Ending program...")
	os.system("pause")
	exit()