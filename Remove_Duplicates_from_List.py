# lst = [1,2,2,3,4,4,5]

# unique = []
# for item in lst:
#     if item not in unique:
#         unique.append(item)
        
# print(unique)

lst = [1,2,2,3,4,4,5]
unique = list(set(lst))
print(unique)