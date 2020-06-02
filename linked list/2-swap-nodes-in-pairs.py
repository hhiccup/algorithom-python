# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
class Solution: #官方迭代法
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            # Nodes to be swapped
            first_node = head;
            second_node = head.next;

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next


class Solution: #test1  递归法 71%
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        node1 = head
        node2 = head.next

        node1.next = self.swapPairs(node2.next)
        node2.next = node1

        return node2

'''

class Solution: #test2  迭代法  波动大%
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(1)
        dummy.next = head #当只有一个节点时

        prev_node = dummy
        while head and head.next:
            node1 = head
            node2 = head.next

            prev_node.next = node2 #把这一对的2地址接到上一对的最后
            node1.next = node2.next #对调  
            node2.next = node1 #对调

            head = node1.next #下一对节点的1地址传下去
            prev_node = node1 #保存这一对节点的2地址（节点），用在下一轮中衔接下一对调换后的地址

        return dummy.next
