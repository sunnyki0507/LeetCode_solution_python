class Solution(object):
    def findSubstring(self, s, words):

        res = []
        length = len(words[0])
        num = len(words)
        add = length * num
        i = 0
        
        copy = set(words[:]) 
        if len(copy) == 1:
            compare = "".join(words)
            while i < len(s)-add+1:
                new = s[i:i+add]
                if new == compare:
                    res.append(i)
                i += 1

        else:
            while i < len(s)-add+1:
                new = s[i:i+add]
                j = 0
                c = words[:]
                while j < add:
                    check = new[j:j+length]
                    if check in c:
                        idx = c.index(check)
                        c.pop(idx)
                    else:
                        break
                    j += length
                if not c:
                    res.append(i)
                i += 1
        return res


        # res = []
        # length = len(words[0])
        # # check = words[:]
        # # tmp = []
        # # idx = 0
        # # print(length)
        # # print(check)
        # for j in range(length):
        #     i = j
        #     idx = j
        #     tmp = []
        #     check = words[:]
        #     while i < len(s):
        #         c = s[i:i+length]
        #         # print(i)
        #         # print(c)
        #         if c in check:
        #             # print("Hi")
        #             eraseI = check.index(c)
        #             tmp.append(check.pop(eraseI))
        #             i += length
        #             # print(i)
        #             if not check:
        #                 if idx not in res:
        #                     res.append(idx)
        #                 check.append(tmp.pop(0))
        #                 idx += length
        #         else:
        #             if c not in words:
        #                 i += 1
        #                 idx = i
        #                 check = words[:]
        #                 tmp = []
        #                 continue
        #             erase = tmp.pop(0)
        #             check.append(erase)
        #             idx += length
        #             while erase != c and tmp:
        #                 erase = tmp.pop(0)
        #                 check.append(erase)
        #                 idx += length
        #             eraseI = check.index(c)
        #             tmp.append(check.pop(eraseI))
        #             i += length
        #             if not check:
        #                 if idx not in res:
        #                     res.append(idx)
        #                 check.append(tmp.pop(0))
        #                 idx += length
        # return res

                    






        # res = []
        # length = len(words[0])
        # c = words[:]
        # idx = 0
        # fir = 0
        # tmp = []
        # while fir < len(s):
        #     new = s[fir: fir + length]
        #     print(new)
        #     print(tmp)
        #     if new not in c:
        #         # c = words[:]
        #         arr = tmp.pop(0)
        #         c.append(arr)
        #         idx += length
        #         while arr != new and tmp:
        #             arr = tmp.pop(0)
        #             c.append(arr)
        #             idx += length
        #         if new not in words:
        #             idx += length
        #         else:
        #             i = c.index(new)
        #             tmp.append(c.pop(i))
        #             if not c:
        #                 res.append(idx)
        #                 idx += length
        #                 c.append(tmp.pop(0))
        #                 # c = words[:]
        #     else:
        #         i = c.index(new)
        #         tmp.append(c.pop(i))
        #         if not c:
        #             res.append(idx)
        #             idx += length
        #             c.append(tmp.pop(0))

        #     fir += length
        #     print(fir)
        #     print(idx)
        # return res
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        "ling mind raboo fooo wing ding barr wing monkey pound cake"