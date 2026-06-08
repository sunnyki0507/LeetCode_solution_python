class Solution(object):
    def isIsomorphic(self, s, t):
        sdict = dict()
        tdict = dict()
        slist = list(s)
        tlist = list(t)
        nums = 97
        numt = 97
        while slist:
            sc = slist.pop()
            tc = tlist.pop()
            if sc not in sdict:
                sdict[sc] = chr(nums)
                nums += 1
            if tc not in tdict:
                tdict[tc] = chr(numt)
                numt += 1
        sStr = ""
        tStr = ""
        for i in range(len(s)):
            sc = s[i]
            tc = t[i]
            sStr += sdict[sc]
            tStr += tdict[tc]
        if sStr == tStr:
            return True
        else:
            return False
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        