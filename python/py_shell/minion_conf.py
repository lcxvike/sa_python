#!/usr/bin/python

import os

def id(i):
  grains = {}
  cmd = "ifconfig " + i
  msg = os.popen( cmd ).read().split('\n\n')
  for info in msg:
    lebal = "inet addr"
    post = info.find(lebal)
    if post >= 0:
      tmp = info[post+len(lebal):]
      ip = tmp[:tmp.find(" ")]
      grains["tag"] =  ip.replace('.','-')
  return  grains

def main():
  print id("br0")

if __name__ == '__main__':
  main()
