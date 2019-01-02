def sum_mult(m):
    i = 1
    total = 0
    while m*i < 1000:
        total += m * i
        i += 1
    return total

def multiples():
    sum3 = sum_mult(3)
    sum5 = sum_mult(5)
    sum15 = sum_mult(15)
    
    return sum3 + sum5 - sum15
    
multiples()