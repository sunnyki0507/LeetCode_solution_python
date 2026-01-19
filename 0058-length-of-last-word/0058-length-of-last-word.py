class Solution(object):
    def lengthOfLastWord(self, s):

        length = 0
        adding = True
        for i in s:
            if i != ' ':
                if not adding:
                    adding  = True
                    length = 1
                else:
                    length += 1
            else:
                adding = False
        return length
        # rev = "".join(reversed(s))
        # length = 0
        # for i in rev:
        #     if i == ' ' and length == 0:
        #         continue
        #     if i == ' ':
        #         return length
        #     else:
        #         length += 1
        # return length
        """
        :type s: str
        :rtype: int
        """
        