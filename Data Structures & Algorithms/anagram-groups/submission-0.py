class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word)) # sort the words first

            if sorted_word not in group_anagrams:
                # new sorted words gets added into key with placeholder
                group_anagrams[sorted_word] = []
            # sorted words (new & old) have their value appended with original word 
            group_anagrams[sorted_word].append(word) 

        # return values in list
        return list(group_anagrams.values())