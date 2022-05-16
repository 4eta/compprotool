import random
import time

inf = pow(10,20) + 7

def merge(left, right):  
    sorted_arr = []
    li = 0
    ri = 0
    ls = len(left)
    rs = len(right)
    #get small number
    while li != ls or ri != rs:
        lnow = left[li] if li-ls else inf 
        rnow = right[ri] if ri-rs else inf 
        sorted_arr.append(min(lnow, rnow))
        li += (lnow < rnow)
        ri += (lnow >= rnow)
    #print(sorted_arr)
    return sorted_arr
   
def merge_sort(arr):
    l = len(arr)

    #finish splitting
    if l <= 1:
        return arr

    #split
    mid = l // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)    
    right = merge_sort(right)

    #merge
    return merge(left, right)

def insertion_sort(arr):
    for i in range(1,n):
        t = arr[i]
        j = i-1
        while j >= 0 and arr[j] > t:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = t
    return arr 

n = 5*10**3
a = [random.randint(0, 10000) for _ in range(n)]

start = time.time()
sort_a = merge_sort(a)
#print(merge_sort(a))
end = time.time()
print(f"merge_sort:{end-start}")

start = time.time()
sorted_a = insertion_sort(a)
end = time.time()
print(f"insertion_sort:{end-start}")

n = 20
a = [random.randint(-10000, 10000) for _ in range(n)]
sort_a = merge_sort(a)
print(sort_a)