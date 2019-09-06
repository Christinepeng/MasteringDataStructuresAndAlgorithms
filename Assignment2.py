#Determine if a given string is a Palindrome
# Write a function to determine if a given string is a palindrome ignoring special characters and ignoring
# case. Your algorithm must work in place and not require any extra memory.
class Solution:
    def isPalindrome(self, s):
        n = len(s)

        l = 0
        r = n - 1

        while l < r:
            while l < r and not (s[l].isdigit() or s[l].isalpha()):
                l += 1
            while l < r and not (s[r].isdigit() or s[r].isalpha()):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True


sol = Solution()
test_cases = ['abb', '...........aa', "No!....devil...,.'....lived......on", 'Ma......a.m!']
for test_case in test_cases:
    print(sol.isPalindrome(test_case))


#         return True
#         # ns = [ss.lower() for ss in s if ss.isdigit() or ss.isalpha()]
#         # n = (len(ns) // 2) + 1
#         # return ns[:n] == ns[::-1][:n]