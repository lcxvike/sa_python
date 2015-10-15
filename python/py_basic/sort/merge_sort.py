#!/usr/bin/python

def merge(left,right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += left[r:]
    return result

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left,right)


if __name__ == '__main__':
    seq =[49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    merge_sort(seq)
    print seq 
