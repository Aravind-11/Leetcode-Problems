class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        n=len(needle)
        for i in range(len(haystack)):
            if(haystack[i:n+i]==needle):
                return i
        return -1