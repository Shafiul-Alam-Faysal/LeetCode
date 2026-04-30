data = [10, 15, 20, 25, 30]

def avgmean(data):
    total = 0
    count = 0
    for d in data:
        total += d
        count += 1
        
    mean = total / count
    return mean

print(avgmean(data))