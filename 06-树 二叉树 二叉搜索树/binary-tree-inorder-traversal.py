# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution: #题解 递归模板  时O(n) 空O(h 树高) 
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)

        dfs(root)
        return result

         
class Solution: #题解 递归遍历模板2  
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

'''
class Solution: #test1 题解的迭代法（自己维护一个栈）
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        white, gray = 0, 1
        res = []
        stack = [(white, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == white: #若是其他序遍历，就改下下面的顺序即可，注：要反序压入栈中
                stack.append((white, node.right))
                stack.append((gray, node.val))
                stack.append((white, node.left))
            else:
                res.append(node)
        return res
#层序遍历的话就把stack变成queue，pop就改成pop(0)，因为是先进先出
   
##################2、binary-tree-preorder-traversal#####################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:# try1 直接递归 O(n) O(h)
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
'''

class Solution:# try2   带标记迭代 5min
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [(0, root)]
        while stack:
            flag, node = stack.pop()
            if not node: continue
            if flag == 0:
                stack.append((0, node.right))
                stack.append((0, node.left))
                stack.append((1, node))
            else:
                res.append(node.val)
        return res

