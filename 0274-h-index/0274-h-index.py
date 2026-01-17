class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse = True)

        for i in range(len(citations)):
            if citations[i] >= (i+1):
                continue
            else:
                return i
        return len(citations)
        


        # arr = list(citations)
        # papers = []
        # h = 0
        # while arr:
        #     num = max(arr)
        #     idx = arr.index(num)
        #     papers.append(arr.pop(idx))
        #     if len(papers) <= num:
        #         h = max(h,len(papers))
        #     else:
        #         break
        # return h



        """
        :type citations: List[int]
        :rtype: int
        """
        