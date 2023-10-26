arr = [1,2,2,3]
arr2 = []
for i in arr:
    if i not in arr2:
        arr2.append(i)
print (arr2)