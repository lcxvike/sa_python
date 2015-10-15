#!/usr/bin/python

def partition(lists,left,right):
    key = lists[left]
    while left < right:
        while left < right and lists[right] >= key:
            right = right -1
        while left < right and lists[right] < key:
            lists[left] = lists[right]
            left += 1
            lists[right] = lists[left]
    lists[left] = key
    return left            

def quick_sort(lists,left,right):
    if left < right:
        key_index = partition(lists,left,right)
        quick_sort(lists,left,key_index)
        quick_sort(lists,key_index+1,right)

if __name__ == '__main__':
    seq =[49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    quick_sort(seq,0,len(seq)-1)
    print seq
