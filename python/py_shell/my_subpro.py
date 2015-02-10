#!/usr/bin/env python

import subprocess

def multi(*args):
	for cmd in args:
		p = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
		outs = p.stdout.readlines()
		for out in outs:
			print out,
def main():
	print "="*15 + "begin" + "="*15
	multi('hostname', 'df -Th', 'ls -l /tmp', 'tail /var/log/messages')

if __name__ == '__main__':
	main()
