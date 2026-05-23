class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        record = {}
        final_list = []

        # Number as key, count as value
        for num in nums:
            if num in record:
                record[num] = record[num] + 1
            else:
                record[num] = 1

        # Search the max using value
        # Append to list
        # Remove from dictionary & repeat
        for i in range(k):
            key_with_highest_value = max(record, key=record.get)
            final_list.append(key_with_highest_value)
            record.pop(key_with_highest_value)

        return(final_list)