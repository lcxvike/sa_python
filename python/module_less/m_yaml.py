#!/usr/bin/python

import yaml
h_info = yaml.load(file('/export/leicx/soft/sa_dev/python/config/name.yaml'))
print h_info['name']
print h_info['manager']['touch']['ip_test']

