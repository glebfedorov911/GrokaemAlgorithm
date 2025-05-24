from typing import Optional, Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        list_node = self
        while list_node:
            yield list_node.val
            list_node = list_node.next

class Solution:


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_nums = []
        while list1 or list2:
            if list1 and list2 :
                if list1.val <= list2.val:
                    sorted_nums.append(list1.val)
                    list1 = list1.next
                elif list2.val <= list1.val:
                    sorted_nums.append(list2.val)
                    list2 = list2.next
            else:
                if list1:
                    sorted_nums.append(list1.val)
                    list1 = list1.next
                if list2:
                    sorted_nums.append(list2.val)
                    list2 = list2.next

        if not sorted_nums:
            return

        result_node = ListNode(sorted_nums[-1])
        for num in sorted_nums[:-1][::-1]:
            temp = ListNode(num)
            temp.next = result_node
            result_node = temp

        return result_node

node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
node2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

s = Solution()
r = s.mergeTwoLists(node1, node2)
print(r)
for i in r:
    print(i)