class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        c=[]
        for i in range(len(s)):
            if len(c)!=0:
                if c[-1]==s[i]:
                    c.pop()
                else:
                    c.append(s[i])
            else:
                c.append(s[i])
        return "".join(c)