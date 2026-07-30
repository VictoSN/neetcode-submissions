class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for x, y in enumerate(nums):
            nums_dict[y] = x
        
        for x, y in enumerate(nums):
            different = target - y # findout the number to get to target

            # search for diff in current dict
            if different in nums_dict and x != nums_dict[different]:
                # if found, return current index and diff's index
                return [x, nums_dict[different]]
        
        return []