# sotring functions / Lia McClane
# selection sort

def selectionSort(arr):
    minIndex = 0
    for i in range(len(arr)):
        minInt=arr[i]
        for j in range(i + 1, len(arr)):
            # print(f"i = {i} j = {j}") 
            if arr[j]<minInt:
                minInt = arr[j]
                minIndex = j
        temp = arr[i]
        arr[i] = minInt
        arr[minIndex] = temp
        # print(arr)
    return arr
print([55,33,44,77,11,33,100])
print(selectionSort([55,33,44,77,11,33,100])) 

print([44,1])
print(selectionSort([44,1]))