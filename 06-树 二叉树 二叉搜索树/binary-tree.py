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



################# 4 二叉树的最小深度 ###############

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif not root.left and not root.right: # 当前节点没有子节点时，才算是到底了，返回深度
            return 1  #可优化， 此条件判断可与下面的合并一个！！
        else:   # !!!注意 ：当前节点只有一个子节点时，要拿到的是子节点的深度，并不是返回1，所求并没有结束
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
 '''

class Solution: # 光头哥 。。。
    def minDepth(self, root):
        if not root: return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)      

class Solution: # BFS  国际站  
    def minDepth(self, root):
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))



#################### 5  二叉树的序列化与反序列化 （困难） ##########################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        valList = []
        def recur(node):
            if node:
                valList.append(str(node.val))
                recur(node.left)
                recur(node.right)
            else:
                valList.append('#')
        recur(root)
#        print(valList)
        return ','.join(valList)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        value = iter(data.split(','))
        def recur():
            val = next(value)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = recur()
            node.right = recur()
            return node
        return recur()

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



################### 6 最近公共祖先 （中）########################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: #test1 看题解后写
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: #终止条件
            return root
        #获取左右子节点信息
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        #回溯
        if not left: 
            return right
        if not right:
            return left
        return root

            

###################### 7 从前序和中序遍历构造二叉树   ############################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # 看过题解后  这种最易懂
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0]) #获取前序中的根节点在中序中的索引，用于后面切割二者

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root


class Solution: # 看过题解后  用哈希表（字典）优化   （内存击败100%！）
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        hashmap = {v:i for i,v in enumerate(inorder)}

         #使用左闭右开区间，即preorder[p1,p1)和inorder[i2,i2)
        def recur(preorder, p1, p2, inorder, i1, i2):
            if p1 == p2:
                return None
            root = TreeNode(preorder[p1])

            mid = hashmap[preorder[p1]] #获取前序中的根节点在中序中的索引，用于后面切割二者

            root.left = recur(preorder, p1+1, p1+1+mid-i1, inorder, i1, mid)
            root.right = recur(preorder, p1+1+mid-i1, p2, inorder, mid+1, i2)
            return root
        return recur(preorder, 0, len(preorder), inorder, 0, len(inorder))
