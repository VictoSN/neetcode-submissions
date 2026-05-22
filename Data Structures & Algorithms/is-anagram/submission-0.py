class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        anagram2 = {}

        # Add every letter into a dictionary with their count
        for i in s:
            if i in anagram:
                anagram[i] = anagram[i] + 1
            else:
                anagram[i] = 1

        for i in t:
            if i in anagram2:
                anagram2[i] = anagram2[i] + 1
            else:
                anagram2[i] = 1
        
        # Compare the 2 dictionaries
        if anagram == anagram2:
            return True
        return False