class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        rlist = list(ransomNote)
        mlist = list(magazine)
        while rlist:
            ch = rlist.pop()
            if ch in mlist:
                mlist.remove(ch)
            else:
                return False
        return True
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        