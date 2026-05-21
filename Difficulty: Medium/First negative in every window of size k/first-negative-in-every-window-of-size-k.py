#User function Template for python3

from collections import deque

class Solution:
    def firstNegInt(self, arr, k): 
        q = deque()
        result = []

        
        for i in range(k):
            if arr[i] < 0:
                q.append(i)

        if q:
            result.append(arr[q[0]])
        else:
            result.append(0)

        
        for i in range(k, len(arr)):

            
            while q and q[0] <= i - k:
                q.popleft()

            
            if arr[i] < 0:
                q.append(i)

            
            if q:
                result.append(arr[q[0]])
            else:
                result.append(0)

        return result    
                 
