class Solution(object):
    def romanToInt(self, s):
        dic = {}
        dic['I'] = 1
        dic['V'] = 5
        dic['X'] = 10
        dic['L'] = 50
        dic['C'] = 100
        dic['D'] = 500
        dic['M'] = 1000

        result = dic[s[0]]
        for i in range(1, len(s)):
            if dic[s[i-1]] < dic[s[i]]:
                result = result - (dic[s[i-1]]*2) + dic[s[i]]
                continue
            result += dic[s[i]]
        return result

            

        """
        :type s: str
        :rtype: int
        """
        