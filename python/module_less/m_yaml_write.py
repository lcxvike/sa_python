#!/usr/bin/python

import yaml
import os

filedir = "/export/leicx/soft/sa_dev/python/config"
filename = "name.yaml"
file = os.path.join(filedir,filename)

f = open(file)
s = yaml.load(f)
f.close()

def jx_list(i):
  for n in i:
    if type(n) == list:
      jx_list([n])
      print(i,n)
    elif type(n) == dict:
      jx_dict(n)
    else:
      print(n)

def jx_dict(i):
  for n in i:
    if type(i[n]) == dict:
      jx_dict(i[n])
    elif type(i[n]) == list:
      jx_list(i[n])
      pass
    else:
      print(n,i[n]) 

w_filename = "soft_ip.yaml"
w_file = os.path.join(filedir,w_filename)  
data={'host': {'ip01': {'two': '192.168.1.254', 'one': '192.168.1.2'}, 'ip00': '192.168.1.1'}, 'soft': {'apache': '2.2', 'php': '5.3', 'mysql': '5.2'}}
h=open(w_file,'w')
yaml.dump(data,h)
h.close()


if __name__ == "__main__":
  for i in s:
    if type(s[i]) == dict:
      jx_dict(s[i])
    if type(s[i]) == list:
      jx_list(s(i))
