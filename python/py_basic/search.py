#!/usr/bin/python

def search(lists,num,lower=0,upper=None):
    if upper is None: upper = len(lists)-1
    if lower == upper:
        assert num == lists[upper]
        return upper
    else:
        middle = (lower+upper)//2
        if num > lists[middle]:
            return search(lists,num,middle+1,upper)
        else:
            return search(lists,num,lower,middle)

if __name__ == '__main__':
    seq =[4, 8, 15, 17, 26, 33, 47, 59, 65, 74]
    print search(seq,17)
    
