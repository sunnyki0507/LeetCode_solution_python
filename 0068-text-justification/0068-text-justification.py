class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        add = []
        string = ""
        for i in words:
            print(i)
            if len(string) == 0:
                string += i
                add.append(i)
                continue
            else:
                if (len(string) + len(i) + 1) <= maxWidth:
                    string += " "
                    string += i
                    add.append(i)
                else:
                    print(add)
                    left = maxWidth - len(string)
                    gap = len(add) - 1
                    if gap == 0:
                        gap = 1
                    for j in range(left):
                        add[j%gap] += " "
                    res.append(" ".join(add))
                    string = i
                    add = []
                    add.append(i)

        if add:
            left = maxWidth - len(string)
            for j in range(left):
                string += " "
            res.append(string)
        return res
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        