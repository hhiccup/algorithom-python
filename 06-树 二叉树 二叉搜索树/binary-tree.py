################### 1 验证二叉搜索树 #####################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution: #test1 参考题解写出  中序遍历法
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float('-inf') # 负无穷！！！
        stack = [(0,root)]
        while stack:
            flag, cur = stack.pop()
            if cur == None: continue
            if flag == 0:
                stack.append((0,cur.right))
                stack.append((1,cur))
                stack.append((0,cur.left))
            elif cur.val <= pre:
                return False
            else:
                pre = cur.val
        return True

class Solution: #test1-2 参考题解写出  递归法
    def isValidBST(self, root: TreeNode) -> bool: 

        def helper(node, floor = float('-inf'), celing = float('inf')):
            if not node:
                return True
            if node.val <= floor or node.val >= celing: #!!!!!注意 等于也不可以！！！
                return False
            if not helper(node.left, floor, node.val):
                return False
            if not helper(node.right, node.val, celing):
                return False
            return True
        return helper(root)
'''        
     
class Solution: #test2-1  递归法 6-7min
    def isValidBST(self, root: TreeNode) -> bool: 
        def recur(node, floor = float('-inf'), celing = float('inf')):
            if not node:return True
            if node.val <= floor or node.val >= celing:
                return False
            
            if not recur(node.left, floor, node.val):
                return False
            if not recur(node.right, node.val, celing):
                return False
            return True
        
        return recur(root)
        
        
        
        
        
        
        
################### 2 翻转二叉树 ########################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution: #try1  第一次做，几分钟写完！！！
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def recur(node):
            if not node:
                return
            tmp = node.left
            node.left = node.right
            node.right = tmp

            if node.left:   recur(node.left)
            if node.right:  recur(node.right)
        recur(root)
        return root


class Solution: #上面的递归法 优化 （光头哥）
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        #未写return 函数会默认返回None对象！！  可利用
'''

'''
class Solution: #try2 迭代  第一次写，5min写出
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur:             #可以交给循环默认略过
                continue
            tmp = cur.left          # python 在这里可以直接交换赋值 ！！！
            cur.left = cur.right    # python 在这里可以直接交换赋值 ！！！
            cur.right = tmp         # python 在这里可以直接交换赋值 ！！！
            stack.append(cur.left)  #可用 += 简化
            stack.append(cur.right) #可用 += 简化
        return root
'''
class Solution: #照光头哥的优化下
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                cur.left, cur.right = cur.right, cur.left
                stack += cur.left, cur.right
        return root

################### 3 二叉树的最大深度 ########################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution: #try1 第一次写 几分钟完
    def maxDepth(self, root: TreeNode) -> int:
        maxD = 0
        def recur(node, maxD):
            if not node:
                return maxD
            else: maxD += 1
            tmp1 = recur(node.left, maxD)
            tmp2 = recur(node.right, maxD)
            return max(tmp1, tmp2)
        return recur(root, maxD)

class Solution: # 看完光头哥 优化
    def maxDepth(self, root: TreeNode) -> int:  # 函数里面只有if 和 else 就可以优化成一行写法并放到return里
        if not root:
            res = 0
        else:
            res = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return res
'''
class Solution: # 看完光头哥 最终优化
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

