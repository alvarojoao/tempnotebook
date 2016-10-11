#!/bin/python
def insertionSort(ar):    
    prev = None
    if len(ar)>0:
        prev = ar[0]
    else:
        return
    for i in range(1,len(ar)):
        if ar[i]>prev:
            prev=ar[i]
        else:
            stop = True
            j = i-1
            while(stop):
                if j>=0 and i>=0 and ar[j] > ar[i]:
                    tmp = ar[i]
                    ar[j],ar[i]=ar[j],ar[j]
                    print " ".join(map(str,ar))
                    ar[j]=tmp
                    j=j-1
                    i=i-1

                else:
                    stop =False
    print " ".join(map(str,ar))


m =  10
ar = [2,3,4,5,6,7,8,9,10,1]
insertionSort(ar)
