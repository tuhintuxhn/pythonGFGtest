#User function Template for python3

class Solution:
    def longestUniqueSubstring(self, s):
        maxlen = 0
        left = 0
        st = set()
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            st.add(s[right])
            maxlen = max(maxlen,right-left+1)
        return maxlen    