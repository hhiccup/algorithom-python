# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
class Solution: #test1  暴力/哈希表 ON ON   30-95%
    def hasCycle(self, head: ListNode) -> bool:
        #不需要先处理空或单个节点，循环有能力处理
        hashtb = {}
        while head: #head != None: #该地址里是None？ 还是说
            if head in hashtb:
                return True
            hashtb[head] = 1

            head = head.next
        return False
    # test1 一遍就过

'''

class Solution: #test1  快慢指针法  ON  O1  73%
    def hasCycle(self, head: ListNode):
        if not head or not head.next: #判断前两个节点存在情况
            return False
        head2 = head.next  #前一步需要判断一下才有这一步
        while head2 and head2.next:
            if head == head2:
                return True
            head = head.next
            
            head2 = head2.next.next #这一步需要先保证head2.next存在即可

        return False
        #经过修改后简洁了
