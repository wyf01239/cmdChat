from encodings import utf_8
utf_8
import os
from modules import wgetChar
# from menu import SingleChat

os.system("title pyChat v0.1 by wyf9 2023.3.18")

print ("pyChat Main Menu")
print ("a / 1. Start a Server")
print ("b / 2. Join a Server")
print ("c / 3. Single Chat")
print ("q / e / 0. Quit")
print ("\n")

while True: 
	wChar = wgetChar.wMain()

	match wChar:

		case "a" | "1":
			print ("Server Mode Not Available.")

		case "b" | "2":
			print ("Console Mode Not Available.")

		case "c" | "3":
			print ("================================")
			print ("Single Chat Mode")
# 			SingleChat.wMain()
			print ("================================")

		case "q" | "0" | "e":
			print ("================================")
			print ("Quitting Program...")
			break

os.system("title    ")
exit