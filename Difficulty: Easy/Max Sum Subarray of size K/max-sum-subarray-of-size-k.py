class Solution:
    def maxSubarraySum(self, arr, k):
        
        currentsum = sum(arr[:k])
        maxsum = currentsum 
        for i in range (k , len(arr)):
            currentsum=currentsum + arr[i] - arr[i-k]
            maxsum = max(maxsum , currentsum)
        return maxsum    
        