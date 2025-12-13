class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        def is_valid(s):
            return bool(re.fullmatch(r'[a-zA-Z0-9_]+', s))
        n = len(code)
        
        businesslineset = set(["electronics", "grocery", "pharmacy", "restaurant"])
        codestring = "abcdefghijklmnopqrstuvwxyz0123456789_"

        res = []

        for i in range(n):
            if businessLine[i] not in businesslineset:
                continue

            if not is_valid(code[i]):
                continue

            if not isActive[i]:
                continue
            
            res.append((businessLine[i], code[i]))

        res = sorted(res, key = lambda x : (x[0],x[1]))
        
        ans = []

        for a, b in res:
            ans.append(b)

        return ans