'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
        newNode = Node(val)
        if pos == 1 :
            newNode.next = head
            return newNode
          
        curr = head 
        for i  in range(1 , pos -1):
            curr = curr.next
        
        
        newNode.next = curr.next
        curr.next = newNode
        
        return head
        
      