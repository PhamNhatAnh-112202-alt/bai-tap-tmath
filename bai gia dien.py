    n = int(input())
    if n <= 100:
        tien = n * 2000
    elif n <= 200:
        tien = 100 * 2000 + (n-100) * 3000    
    elif n <= 300:
        tien = 100 * 2000 + 100 * 3000 + (n - 200) * 5000
    else:
        tien = 100 * 2000 + 100 * 3000 + 100 * 5000 + (n-300) * 10000
    print(tien)    
        
