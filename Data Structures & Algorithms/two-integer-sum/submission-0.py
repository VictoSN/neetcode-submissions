class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        ### O(n2) with nested for loop ###
        found = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                # Loop while i and j are not the same
                if nums[i] + nums[j] == target and i != j:
                    answer.extend([i, j])
                    found = True
                    break
            if found:
                break
        return answer