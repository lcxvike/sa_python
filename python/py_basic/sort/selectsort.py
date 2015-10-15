#!/usr/bin/python

def select_sort(lists):
    count = len(lists)
    if count < 2:
        return  lists
    for i in range(0, count):
        min = i
        for j in range(i+1,count):
            if lists[min] > lists[j]:
                min = j
        lists[min],lists[i] = lists[i],lists[min]
    return lists

if __name__ == '__main__':
    seq =[49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    select_sort(seq)
    print seq
