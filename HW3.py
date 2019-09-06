# X419-01: Homework 3
# 1.-Reverse a queue using recursion.
# class Solution:
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

    def printQueue(self):
        for i in self.items:
            print(i, end = " ")


def reverseQueue(q):
    if (q.isEmpty()):
        return
    s = q.front();
    q.pop();
    reverseQueue(q)
    q.add(s)


q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.add(5)
q.add(6)
q.add(7)
q.add(8)
q.add(9)
q.add(10)
reverseQueue(q)
q.printQueue()
#     def __init__(self):
#         self.items = []
#
#     # def printQueue(self):
#     #     for i in self.items:
#     #         print(i, end = " ")
#     #     print("")
#     def pop(self):
#         return self.items.pop(0)
#
#     def _reverseQueue(self, q):
#         if q.empty():
#             return q
#         else:
#             s = q.peek()
#             q.pop()
#
#     def reverseQueue(self, q):
#         self._reverseQueue(q)
#         q.append(s)
#
# sol = Solution()
# print(sol.reverseQueue([1, 2, 3, 4, 5]))
#
#
#
#     q.printQueue()
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def add(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop(0)
#
#     def front(self):
#         return self.items[0]
#
#     def printQueue(self):
#         for i in self.items:
#             print(i, end = " ")
#         print("")
#
# def reverseQueue(self, q):
#     if q.isEmpty():
#         return q
#     data = q.front()
#     q.pop()
#     reverseQueue(q)
#     q.add(data)
#
# # sol = Solution()
# # print(sol.reverseQueue(1, 2, 3, 4, 5))


# 2.-Check for the following symbols to be balanced on a given string/text file: {}[]()<>.
# Note: the following is not considered balanced: {<}>; but this is: {}<>
class Solution:
    def isBalanced(self, s):
        if s == '':
            return True

        lst = []
        dict_br = {'}': '{', ']': '[', ')': '(', '>': '<'}

        for ss in s:
            if ss not in dict_br:
                lst.append(ss)
            else:
                if lst != [] and (lst[-1] == dict_br.get(ss)):
                    lst.pop()
                else:
                    return False
        return (len(lst) == 0)

#stacks method, add element which hasn't been match. Finally, we should get an empty list at the end.
#Time complexity: O(n)
#Space complexity: O(n)


#two problem in the same file, use one class or two classes?
