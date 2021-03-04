from typing import List

'''2021/03/04'''
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
你可以按任意顺序返回答案。
"""


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        # 方法1.  36ms    14.8MB
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # 方法2.  28ms    15MB
        hashmap = {}
        for ind, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [ind, hashmap.get(target - num)]
            hashmap[num] = ind
            print(hashmap, hashmap.get(num))
