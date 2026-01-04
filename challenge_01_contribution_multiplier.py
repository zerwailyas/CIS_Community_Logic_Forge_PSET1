def cal_impact(contributions)-> list:

    n = len(contributions)
    if n <= 0:
        return []

    impacts = [1] * n

    
    left_prod = 1
    for i in range(n):
        impacts[i] = left_prod
        left_prod *= contributions[i]

    
    right_prod = 1
    for i in range(n - 1, -1, -1):
        impacts[i] *= right_prod    
        right_prod *= contributions[i]

    return impacts

test_contributions = [2, 4, 6, 8]
# impacts should be = [192,96,64,48]
print("Input: [2, 4, 6, 8], and Output: ", cal_impact(test_contributions))