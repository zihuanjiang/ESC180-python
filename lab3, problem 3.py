def pi_function(n):
    total = 0
    for i in range(0,n+1):
        total += (-1)**i/(2*i+1)
    total *= 4
    return total

print(pi_function(1000))