#example input: 3 0 2 6 8 1 7 9 4 2 5 5 0
#example output: [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]]


from typing import Optional,List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        rows = m  
        columns = n  
        matrix = [[-1 for j in range(columns)] for i in range(rows)]
        current=head
        i=0
        j=0
        direction=0
        while current:
            matrix[i][j] = current.val
            current=current.next
            if direction == 0:  # moving right
                if j<n-1 and matrix[i][j + 1] == -1:
                    j += 1
                else:
                    direction = 1
                    i += 1
            elif direction == 1:  # moving down
                if i<m-1 and matrix[i + 1][j] == -1:
                    i += 1
                else:
                    direction = 2
                    j -= 1
            elif direction == 2:  # moving left
                if j > 0 and matrix[i][j - 1] == -1:
                    j -= 1
                else:
                    direction = 3
                    i -= 1
            elif direction == 3:  # moving up
                if i > 0 and matrix[i - 1][j] == -1:
                    i -= 1
                else:
                    direction = 0
                    j += 1
        
        return matrix

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

elements = list(map(int, input("Enter elements of your linked list (space-separated): ").split()))
rows=int(input("Enter the number of rows of matrix:\n"))
columns=int(input("Enter the number of column of matrix:\n"))
head = create_linked_list(elements)
sol = Solution() 
output=sol.spiralMatrix(rows,columns,head)
print(f"the spiral matrix is:\n{output}")       