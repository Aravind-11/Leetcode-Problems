class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        end=begin=max_len=0
        a={}
        while(end<len(s)):
            endchar=s[end]
            if(endchar in a and a[endchar]>=begin):
                begin=a[endchar]+1
            else:
                a[endchar]=end
                end+=1
            if(end-begin>max_len):
                max_len=end-begin
        return max_len
        