#!/usr/bin/env python

import paramiko
import getpass

username='root'

def remote_ssh_exec(port, username, hostname, password, cmd):
	m_ssh = paramiko.SSHClient()
	m_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	m_ssh.connect(hostname = hostname,port=port,username=username, password=password)
	stdin,stdout,stderr=m_ssh.exec_command(cmd)
	#print stdout.readline()
	for out in stdout.readlines():
		print out,
	m_ssh.close()

def main():
	print "="*15 + "begin" + "="*15
	hostname='10.87.66.11'
	print hostname
	port = int(raw_input("port:"))
	password = getpass.getpass('please input password:')
	remote_ssh_exec(port, username, hostname, password, 'hostname')
	remote_ssh_exec(port, username, hostname, password, 'df -Th')

if  __name__ == '__main__':
	main()
