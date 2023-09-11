# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        main = ListNode()
        node = main
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap,(lists[i].val,i))
                
        while heap:
            nd = heappop(heap)
            node.next = ListNode(nd[0])
            node = node.next
            if lists[nd[1]].next:
                lists[nd[1]] = lists[nd[1]].next
                heappush(heap,(lists[nd[1]].val,nd[1]))
                
        return main.next
        
        
            
        
        