nums = [6,6,5,5,4,1]
sum = 0
flag_1 = True
flag_2 = True

for i in range(1, len(nums)-1):
    left, right = i-1, i+1
    while left >= 0 and right < len(nums):
        if nums[left] == nums[i]:
            left -= 1
        elif nums[right] == nums[i]:
            right += 1
        else:
            break
    if left >= 0 and right < len(nums):
        if nums[left] < nums[i] and nums[right] < nums[i] and flag_1:
            sum += 1
            flag_1 = False
            flag_2 = True
        elif nums[left] > nums[i] and nums[right] > nums[i] and flag_2:
            sum += 1
            flag_1 = True
            flag_2 = False
print(sum)