lst = [4, 1, 7, 9, 2]

def find_max(lst):
    temp = lst[0]
    for num in lst:
        if num > temp:
            temp = num
    return temp

print(find_max(lst))