# Definition for a binary tree node.
# https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printPreOrder(self, n):
        if n is None:
            return
        print(n.val);
        self.printPreOrder(n.left)
        self.printPreOrder(n.right)

    def sortedArrayToBSTHelper(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTHelper(nums, start, mid - 1)
        root.right = self.sortedArrayToBSTHelper(nums, mid + 1, end)
        return root

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #print("sortedArrayToBST: array: ", nums)
        result = self.sortedArrayToBSTHelper(nums, 0, len(nums) - 1)
        return result

a = [-10, -3, 0, 5, 9]
#a = [0, -3, 9, -10, null , 5
solution = Solution()
solution.printPreOrder(solution.sortedArrayToBST(a))
