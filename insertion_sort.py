import random
import time
n = 5000
a = [random.randint(0, 10000) for _ in range(n)]
    
def insertion_sort(arr):
    for i in range(1,n):
        t = arr[i]
        j = i-1
        #sort済みの配列の中で良い感じに入れるところを探す
        while j >= 0 and arr[j] > t:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = t
    return arr 
    

start = time.time()
sorted_a = insertion_sort(a)
end = time.time()
print(sorted_a[:20],sorted_a[-20:])
print(f"{end-start} sec")