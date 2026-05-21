class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = None
        nums.sort()
        for i in range(len(nums)):
            print(nums[i], duplicate)
            if nums[i] == duplicate:
                return True
            # store value and move to the next value
            duplicate = nums[i]
        return False