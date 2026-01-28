class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        counter = 1
        longest = 1 

        if not nums:
            return 0

        for i in range(1,len(nums)):

            if nums[i] == nums[i-1]:
                continue

            if nums[i-1] + 1 == nums[i]:
                counter += 1
                if longest < counter:
                    longest = counter

            else:
                counter = 1

        return longest