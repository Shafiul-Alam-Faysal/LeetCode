rainfall = [0, 12, 5, 0, 20, 7, 0]

def rainfallstate(data):
    total = 0
    rainy_days = 0
    
    for d in data:
        total += d
        if d > 0:
            rainy_days += 1
            
    avg = total / len(data)
    
    return total, avg, rainy_days

print(rainfallstate(rainfall))