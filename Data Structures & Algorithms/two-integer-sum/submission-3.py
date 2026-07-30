class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for x, y in enumerate(nums):
            nums_dict[y] = x
        
        for x, y in enumerate(nums):
            different = target - y
            if different in nums_dict and x != nums_dict[different]:
                return [x, nums_dict[different]]
        
        return []