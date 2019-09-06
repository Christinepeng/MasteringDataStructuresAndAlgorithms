class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _is_symmetric(self, lroot, rroot):
        if lroot == None and rroot == None:
            return True
        elif lroot == None or rroot == None:
            return False
        elif lroot.val == rroot.val:
            return self._is_symmetric(lroot.left, rroot.right) and self._is_symmetric(lroot.right, rroot.left)
        else:
            return False

    def is_symmetric(self, root):
        if root == None:
            return True
        else:
            return self._is_symmetric(root.left, root.right)


def list_to_tree(lst):
    head = lst


#test case
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = None
root.left.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(3)
print(sol.is_symmetric(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(sol.is_symmetric(root))

