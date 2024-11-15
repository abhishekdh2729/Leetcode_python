def twosums(sums):
    n=len(sums)
    target=9
    for i in range(n):
        for j in range(i+1,n):
            if sums[i]+sums[j]==target:
                return [i,j]
    return []
sums=[2,7,11,15]
print(twosums(sums))
