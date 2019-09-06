#Given an unsorted array with N elements find the k-th highest given that k << N

import queue


def solve(arr, k):
    assert (len(arr) > k)  # there must be at least (k+1) elements in `arr`, given k is 0-indexed

    q = queue.PriorityQueue()
    for e in arr:
        if q.qsize() == k + 1:
            top_e = q.get()  # smallest element in PriorityQueue
            max_e = max(top_e, e)
            q.put(max_e)
        else:
            q.put(e)

    for i in range(k - 1):  # pop (k-1) elements from PriorityQueue
        q.get()
    print(q.get())  # print out the k-th element


def main():
    solve([9, 1, 3, 4], 2)


if __name__ == '__main__':
    main()





from Queue import PriorityQueue


# class Solution:
#     def kth_highest(self, arr, k):
#         h = []
#         if k == 0:
#             return None
#         if arr == []:
#             return None
#         for v in arr:
#             if len(h) < k:
#                 h.heappush(h, v)
#             elif len(h) == k:
#                 if h[0] < v:
#                     h.heappushpop(h, v)
#         return h[0]
#
#
# sol = Solution()
# print(sol.kth_highest([4, 5, 6, 2], 2))













#naive approach
#sort(), lst[-k]
# class Solution:
#     def kth_highest(self, lst, k):
#         if lst == []:
#             return
#         else:
#             lst.sort()
#             return lst[-k]
#
# sol = Solution()
# print(sol.kth_highest([4, 5, 6, 2], 2))

# sol = Solution()
# test_cases = [([], 3), ([4, 5, 6, 2], 2), ([1, 1, 1, 1, 1, 1], 2)]       **Error
# for test_case in test_cases:
#     print(sol.kth_highest(test_case))

#Time complexity: O(nlog(n)) + O(1) = O(nlog(n))
#Space complexity: None


#better solution
