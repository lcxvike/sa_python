#!/usr/bin/python

import math

def radix_sort(lists, radix=10):
    k = int(math.ceil( math.log(max(lists),radix) ))
    bucket =  [[] for i in range(radix)]
    for n in range(1,k+1):
        for val in lists:
            bucket[val%(radix**n)/(radix**(n-1))].append(val)
        del lists[:]
        for each in bucket:
            lists.extend(each)
        bucket =  [[] for i in range(radix)]
    return lists

if __name__ == '__main__':
    seq =[49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    radix_sort(seq)
    print seq 
