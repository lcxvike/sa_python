#!/usr/bin/python

def insert_sort(lists):
    count = len(lists)
    if count < 2:
        return  lists
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j = j -1
    return lists

if __name__ == '__main__':
    seq =[6,5,3,1,8,7,2,4]
    insert_sort(seq)
    print seq
    
