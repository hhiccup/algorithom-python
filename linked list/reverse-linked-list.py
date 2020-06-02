
#####can not try

class Solution: # try1  无从下手 因为链表基本操作都没见过。。
    def reverseList(self, head: ListNode) -> ListNode:
        if head.next == None:
            return head
        head.next = reverseList(head.next)
        ListNode.val = x
        return reverseList



class Solution: #test1  遍历法 86%  17%
######总结：这里全都是一些关于地址的操作，指来指去的！！因为每个节点中next变量存放的是下一个节点的地址！
    def reverseList(self, head: ListNode) -> ListNode:
        new = None
        cur = head
        while cur: 
            tmp = cur.next
            cur.next = new

            new = cur
            cur = tmp
        return new


class Solution: # test1 递归法  86%
    def reverseList(self, head: ListNode):
        if head == None or head.next == None:
            return head  #这是最后一个节点的地址，也是答案（反转后第一个节点）的地址
        
        cur = self.reverseList(head.next) #第一次得到返回的值就是上mian一句的head地址

        head.next.next = head #把后面一个节点的next内容改成当前节点的地址（也就是让后面的指向前面）

        head.next = None #这个会把反转后最后一个节点的next改为None!

        return cur  #最后那个节点的地址
        
