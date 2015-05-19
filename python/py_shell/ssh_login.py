#!/usr/bin/python

import pexpect

m_ip = '192.168.253.9'
m_user = 'haiwai'
m_port = '22'
m_passwd = '123456'

def ssh_login(ip,user,port,passwd):
  child = pexpect.spawn('ssh -p %s %s@%s' % (port,user,ip))
  child.expect('password:')
  child.sendline(passwd)
  child.interact()
  print "login ok"

def main():
  ssh_login(m_ip,m_user,m_port,m_passwd)

if __name__ == '__main__':
  main()
