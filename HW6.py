class Solution:
    def count_even_amount(self, idx, string):
        if len(string) == idx:
            return 0
        if int(string[idx]) % 2 == 0:
            return 1 + self.count_even_amount(idx+1, string)
        return self.count_even_amount(idx+1, string)

    def count_even_partition(self, string):
        n = len(string)
        if int(string[n-1]) % 2 != 0:
            return 0
        return 2 ** (self.count_even_amount(0, string) - 1)


sol = Solution()
test_cases = ['10', '22', '333']
for test_case in test_cases:
    print(sol.count_even_partition(test_case))