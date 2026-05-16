class Solution:
    def largest(self, arr):
        
        maximum = 0
        for i in range(0 , len(arr)):
            if arr[i]>maximum:
                maximum = arr[i]
           
        return maximum       