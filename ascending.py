lst = [1, 6, 3, 4, 5]

sorted = True

for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        sorted = False
        break

print(sorted)

