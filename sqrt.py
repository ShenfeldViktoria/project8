def my_sqrt(x):
    if x < 2:
        return x
    
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

print(my_sqrt(4))
print(my_sqrt(8))
print(my_sqrt(0))
print(my_sqrt(1))
print(my_sqrt(16))
print(my_sqrt(26))
