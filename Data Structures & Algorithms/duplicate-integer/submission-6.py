class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        validated_set = set(nums)
        if len(nums) != len(validated_set):
            return True
        return False
