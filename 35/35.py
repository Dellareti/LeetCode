class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                if nums[i] > target:
                    return i
                k+=1
        return k