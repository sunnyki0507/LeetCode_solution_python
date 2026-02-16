class Solution(object):
    def minWindow(self, s, t):
        
        n = len(s)
        m = len(t)
        if m > n:
            return ""
        minLen = n+1
        sIdx = 0
        arr = [0] * 256
        for i in range(m):
            arr[ord(t[i])] += 1
        start = 0
        end = 0
        count = 0
        while end < n:
            if arr[ord(s[end])]>0:
                count += 1
            arr[ord(s[end])] -= 1

            while count == m:
                if (end - start + 1) < minLen:
                    minLen = end - start + 1
                    sIdx = start
                
                arr[ord(s[start])] += 1
                if arr[ord(s[start])] > 0:
                    count -= 1
                start += 1
            
            end += 1
        if minLen == n+1:
            minLen = 0
        print(sIdx)
        print(minLen)
        return s[sIdx:sIdx+minLen]

        # if len(t) > len(s):
        #     return ""
        # alpa = []
        # result = []
        # save = []
        # compare = []
        # count = 0
        # for j in range(len(t)):
        #     alpa.append(t[j])
        #     compare.append(t[j])
        # print(compare)
        # for i in range(len(s)):
        #     if s[i] not in alpa and not save:
        #         continue
        #     else:
        #         save.append(s[i])
        #     if s[i] in compare:
        #         count += 1
        #         if s[i] in alpa:
        #             alpa.remove(s[i])
        #         print(s[i])
        #         print(save)               
        #     if not alpa:
        #         print("Hi")
        #         if len(result) == 0:
        #             result = save[:]
        #         else:
        #             result = save[:] if len(save) < len(result) else result
        #         print(save)
        #         # print(result)
        #         count = 0
        #         while save:
        #             c = save.pop(0)
        #             if c in compare:
        #                 count += 1
        #                 if count == 2:
        #                     save.insert(0,c)
        #                     break
        #                 alpa.append(c)
        #         print(alpa)
        # return "".join(result)

        """
        :type s: str
        :type t: str
        :rtype: str
        """
        