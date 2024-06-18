def element_max(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1   
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    if count > len(nums) // 2:
        return candidate
    else:
        raise ValueError("Элемент большинства не найден")
nums = [3, 2, 3]
print(element_max(nums)) 
