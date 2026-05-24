class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        print(nums)
        previous_num = nums[0]
        count_list = []
        current_count = 1

        for num in nums:
            # the first index is not counted
            if previous_num != num:
                # 4 <= 5 [Correct] and 4 >= (5-1) [Correct]
                # 4 <= 6 [Correct] and 4 >= (6-1) [False]
                # 4 <= 4 [Correct] and 4 >= (4-1) [Correct]
                if previous_num <= num and previous_num >= (num - 1):
                    previous_num = num
                    current_count += 1
                else:
                    previous_num = num

                    # Keep track of all the attemps
                    count_list.append(current_count)
                    current_count = 1

        count_list.append(current_count)
        return max(count_list) # Submit the higest count attempt