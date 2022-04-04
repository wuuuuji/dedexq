from typing import List


def minDeletion1(nums: List[int]):
    def sub(data: List[int]):
        dp = [[]]
        for i in data:
            dp.extend([subset + [i] for subset in dp])
        return dp
    subset = sub(nums)



minDeletion1([1,1,2,3,5])


