def pascals_triangle(m):
    '''Returns the mth row (starting from 0) of the Pascal's triangle'''
    current_row = [1]
    for i in range(1,m+1):
        new_row = []
        for j in range(1,len(current_row)):
            new_row.append(current_row[j-1] + current_row[j])
        current_row = [1] + new_row + [1]
    return current_row

def binomial_expansion(a,b,n):
    '''Returns the result of (a+b)**n'''
    coefficients = pascals_triangle(n)
    output = 0
    for k in range(n+1):
        output += coefficients[k] * (a**k) * (b**(n-k))
    return output
