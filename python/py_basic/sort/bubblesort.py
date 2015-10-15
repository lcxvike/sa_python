#!/usr/bin/python

def bubble_sort(lists):
    count = len(lists)
    if count < 2:
        return  lists
    for i in range(0, count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
    return lists

if __name__ == '__main__':
    seq =[49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    bubble_sort(seq)
    print seq
