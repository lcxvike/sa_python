#!/usr/bin/env python

def fibs(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

def main():
    n = int(raw_input('how many Fionacci nuimbers do you want? '))
    print fibs(n)

main()
