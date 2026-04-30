lst = [5, 3, 8, 3, 2, 5, 1]

dup = []
unique = []

for num in lst:
    if num not in unique:
        unique.append(num)
    else:
        if num not in dup:
            dup.append(num)
        
print(dup)
print(unique)