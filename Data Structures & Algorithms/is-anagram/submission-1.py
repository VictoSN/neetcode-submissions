class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        # Use a hash table/dictionary to record 
        # every character and their count
        for ss in s:
            if ss in s_dict:
                s_dict[ss] += 1
            else:
                s_dict[ss] = 1

        for tt in t:
            if tt in t_dict:
                t_dict[tt] += 1
            else:
                t_dict[tt] = 1

        return s_dict == t_dict