class Solution(object):
    def intToRoman(self, num):
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000]+C[(num%1000)//100]+X[(num%100)//10]+I[(num%10)]

        # roman = [(1000,'M'), (900,'CM'), (500,'D'), (400,'CD'), (100,'C'),
        # (90,'XC'),(50,'L'),(40,'XL'),(10, 'X'),(9,'IX'),(5,'V'),(4,'IV'),
        # (1,'I')]

        # out = []

        # for v,c in roman:
        #     count = num // v
        #     num = num - (count*v)
        #     out.append(c*count)
        #     if num == 0:
        #         break
        # return "".join(out)


        # roman = {}
        # roman[1] = 'I'
        # roman[4] = 'IV'
        # roman[5] = 'V'
        # roman[9] = 'IX'
        # roman[10] = 'X'
        # roman[40] = 'XL'
        # roman[50] = 'L'
        # roman[90] = 'XC'
        # roman[100] = 'C'
        # roman[400] = 'CD'
        # roman[500] = 'D'
        # roman[900] = 'CM'
        # roman[1000] = 'M'
        # string = ""

        # strNum = str(num)
        # length = len(strNum)
        # for i in range(length):
        #     n = int(strNum[i])
        #     unit = 10 ** (length-1-i)
        #     if n < 5:
        #         if n == 4:
        #             string += roman[n*unit]
        #             continue
        #         string += (roman[unit] * n)
        #         continue
        #     if n == 9:
        #         string += roman[n*unit]
        #         continue
        #     string += roman[unit*5]
        #     n = n-5
        #     string += (roman[unit] * n)

        # return string

        """
        :type num: int
        :rtype: str
        """
        