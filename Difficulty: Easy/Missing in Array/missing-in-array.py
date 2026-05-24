class Solution:
    def missingNum(self, arr):
        n =len(arr) +1
        expected_sum = n * (n+1) //2
        total_sum = sum(arr)
        return expected_sum - total_sum