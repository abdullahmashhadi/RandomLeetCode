from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        integer1=l1
        integer2=l2
        # num1=''
        # num2=''
        # while(integer1):
        #     num1+=str(integer1.val)
        #     integer1=integer1.next
        # while(integer2):
        #     num2+=str(integer2.val)
        #     integer2=integer2.next
        # sum=0
        # for i in range(len(num1)):
        #     sum+=int(num1[i])*10**i
        # for i in range(len(num2)):
        #     sum+=int(num2[i])*10**i
        # print(sum)
        # dummy_head = ListNode(0)
        # current = dummy_head
        # for i in range(len(str(sum))-1,-1,-1):
        #     current.next=ListNode(int(str(sum)[i]))
        #     current=current.next
        # return dummy_head.next
        sum=0
        left_carry=0
        dummy_head=ListNode(0)
        current=dummy_head
        count=0
        while(integer1 or integer2):
            sum=((integer1.val if integer1 else 0)+(integer2.val if integer2 else 0)+left_carry)
            right_carry=0 if sum<10 else 1
            current.next=ListNode(sum%10)
            current=current.next
            if integer1:
                integer1=integer1.next
            if integer2:
                integer2=integer2.next
            left_carry=right_carry
        if left_carry:
            current.next = ListNode(left_carry)
        return dummy_head.next

def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    elems = []
    current = head
    while current:
        elems.append(current.val)
        current = current.next
    print(elems)

elements1 = list(map(int, input("Enter elements of your linked list (space-separated): ").split()))
elements2 = list(map(int, input("Enter elements of your linked list (space-separated): ").split()))
head1 = create_linked_list(elements1)
head2= create_linked_list(elements2)
sol = Solution() 
new_head = sol.addTwoNumbers(head1,head2)
print("Linked list sum:")
print_linked_list(new_head)       