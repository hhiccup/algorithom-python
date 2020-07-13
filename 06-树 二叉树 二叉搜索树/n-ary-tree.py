
######################1、N叉树的后序遍历#########################

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''
class Solution:# test1-1  看了国际站题解 递归法
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def post(node):
            if node == None:
                return
            for i in node.children:  #1、先子节点
                post(i)
            res.append(node.val)     #2、后根节点
        
        post(root)
        return res
'''
class Solution: #test1-2 国际站 迭代法 
    def postorder(self, root): #比递归快
        res = []
        if root == None: return res
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children)
        return res[::-1]        
        
        
######################2、N叉树的前序遍历#########################

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''
class Solution: #test1-1 递归
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def pre(node):
            if node == None: return
            res.append(node.val)
            for i in node.children:
                pre(i)
        
        pre(root)
        return res
'''
class Solution: #test1-2 迭代法
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None: return res
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children[::-1])  #!! 想清楚顺序！！！！！
        return res
            
######################2、N叉树的层层层层层层层层层层层层层序遍历#########################

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution: #test1 官方题解
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root == None: return res
        deq = collections.deque()
        deq += [root]
        while deq:
            level = []
            for i in range(len(deq)): #知道下一层的子节点个数并遍历取值，取子
                cur = deq.popleft()
                level.append(cur.val)
                deq.extend(cur.children)
            res.append(level)
        return res
            


