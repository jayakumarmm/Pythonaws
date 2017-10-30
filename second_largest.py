arr = '2 3 6 6 5'
arr = [int(x) for x in arr.split()]
arr = list(set(arr))
arr.remove(max(arr))
print (max(arr))











