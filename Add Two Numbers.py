
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        curr=None
        v=0
        while l1 and l2:
            res=l1.val+l2.val+v
            v=0
            if res>9:
                v=int(str(res)[0])
                res=int(str(res)[1])
            new=ListNode(res)
            if not curr:curr=new
            else:
                curr.next=new
                curr=curr.next
            if not head.next:head.next=curr
            l1=l1.next
            l2=l2.next
        while l1:
            res=l1.val+v
            v=0
            if res>9:
                v=int(str(res)[0])
                res=int(str(res)[1])
            new=ListNode(res)
            if not curr:curr=new
            else:
                curr.next=new
                curr=curr.next
            if not head.next:head.next=curr
            l1=l1.next
        while l2:
            res=l2.val+v
            v=0
            if res>9:
                v=int(str(res)[0])
                res=int(str(res)[1])
            new=ListNode(res)
            if not curr:curr=new
            else:
                curr.next=new
                curr=curr.next
            if not head.next:head.next=curr
            l2=l2.next
        if v:
            new=ListNode(v)
            curr.next=new
        return head.next
