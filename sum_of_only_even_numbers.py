lst  = [3, 7, 2, 9, 4]

def sumofeven(lst):
    total = 0
    count = 0
    for num in lst:
        if num % 2 == 0:
            total = total + num
            count += 1
    return total, count

print(sumofeven(lst))