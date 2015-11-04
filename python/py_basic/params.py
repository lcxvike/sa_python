#!/usr/bin/env python
#-*- coding: utf-8 -*-

def params01(*params):
    print params

def params02(title,*params):
    print title
    print params

def params03(**params):
    print params

def params04(x,y,z=1,*pospar,**keypar):
    print x,y,z
    print pospar
    print keypar

def main():
    params01('Test') ##('Test',)说明前面加上一个星号是元组 
    params01(1,2,3)   ##
    params02('params:',1,2,3) ##
    params03(x=1,y=2,z=3) ##
    params04(1,2,3,5,6,7,foo=1,bar=2) ## 
main()
