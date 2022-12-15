x = [1,2,3,4,5,6,7,8,9]

matform = []
count = 3
for i,j in enumerate(x):

    if count == 3:
        matform.append([])
        count = 0
    print(f"Length of matrix: {len(matform)}")
    matform[len(matform)-1].append(j)
    count+=1
print(matform)
