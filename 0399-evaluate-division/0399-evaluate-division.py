class Solution(object):
    def calcEquation(self, equations, values, queries):
        q = {}

        for (a,b), v in zip(equations, values):
            q.setdefault(a, {})[b] = v
            q.setdefault(b, {})[a] = 1.0/v

                
        def f(x,y):
            if x not in q or y not in q:
                return -1.0
            s = [(x,1.0)]
            visited = set()
            while s:
                c, out = s.pop(0)
                visited.add(c)
                if c == y:
                    print(out)
                    return out
                for k in q[c]:
                    if k not in visited:
                        s.append((k, out * q[c][k]))
            return -1.0
        return [f(x,y) for x, y in queries]

            

        
        return [f(x,y) for x, y in queries] 

        
        # n = len(equations)

        # vals = [[] for _ in range(2*n)]

        # mapping = {}

        # idx = 0
        # j = 0
        # for a, b in equations:
        #     if a not in mapping:
        #         mapping[a] = idx
        #         func = values[j] * b
        #         vals[idx].append(func)
        #         idx += 1
        #     else:
        #         strIdx = d[a]
        #         func = values[j] * b
        #         vals[strIdx].append(func)
        #     if b not in mapping:
        #         mapping[b] = idx
        #         func = a / values[j]
        #         vals[idx].append(func)
        #         idx += 1
        #     else:
        #         strIdx = d[b]
        #         func = a / values[j]
        #         vals[idx].append(func)
        #     j += 1
        # print(mapping)
        # print(vals)
        # outcome = []
        # return outcome

        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        