#!/usr/bin/env python

def factorial(num):
    result = num
    for i in range(1,num):
        result *= i
    return result

def main():
    n = int(raw_input('how many Factorial nuimbers do you want? '))
    print factorial(n)

main()
