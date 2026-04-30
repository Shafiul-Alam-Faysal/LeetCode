lst = [10, 15, 20, 25, 30]

div = []

for num in lst:
    if num % 5 == 0 and num % 10 == 0:
        div.append(num)
        
        
print(div)