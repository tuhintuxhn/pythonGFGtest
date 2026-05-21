class Solution:
    def maxSubarraySum(self, arr, k):
        if len(arr) < k:
            return -1 
        currentsum = sum(arr[:k])
        maxsum = currentsum 
        
        for i in range (k , len(arr)):
            currentsum+= arr[i] - arr[i-k]
            maxsum = max(maxsum , currentsum)
        return maxsum    
        