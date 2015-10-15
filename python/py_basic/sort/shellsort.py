#!/usr/bin/python

def shell_sort(lists):
    count = len(lists)
    step = 2
    group = count / step
    if count < 2:
        return  lists
    while group > 0:
        for i in (0,group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k+group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists

if __name__ == '__main__':
    seq =[49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    shell_sort(seq)
    print seq 
