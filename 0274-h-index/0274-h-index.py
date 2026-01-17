class Solution(object):
    def hIndex(self, citations):
        arr = list(citations)
        papers = []
        h = 0
        while arr:
            num = max(arr)
            idx = arr.index(num)
            papers.append(arr.pop(idx))
            if len(papers) <= num:
                h = max(h,len(papers))
            else:
                # h = max(h, num)
                break
        return h



        """
        :type citations: List[int]
        :rtype: int
        """
        