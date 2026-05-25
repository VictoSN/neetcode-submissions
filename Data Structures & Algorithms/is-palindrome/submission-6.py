class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a lower and alpha only string
        s = ''.join(char for char in s.lower() if char.isalnum())
        reverse = s[::-1] # reverse to check for palindrome

        if s == reverse:
            return True
        return False