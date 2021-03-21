#selection sort

l = [19,2,31,45,30,11,121,27]
le=len(l)
for value in range(le):
        min=value
        for j in range(value+1,le):
            if l[min]>l[j]:
                min=j
        l[value],l[min] = l[min],l[value]
print(l)















