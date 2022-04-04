from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    temp1 = set()
    temp2 = set()
    for i in nums1:
        if i not in nums2:
            temp1.add(i)

    for j in nums2:
        if j not in nums1:
            temp2.add(j)
    return [list(temp1), list(temp2)]

print(findDifference([1,2,3,3], [1,1,2,2]))