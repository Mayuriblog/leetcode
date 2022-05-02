class Solution:
    def isValid(self, code: str) -> bool:
        def check(tag):
            n = len(tag)
            if n < 1 or n > 9:
                return False
            return all(c.isupper() for c in tag)

        stk = []
        i, n = 0, len(code)
        while i < n:
            if i and not stk:
                return False
            if code[i: i + 9] == '<![CDATA[':
                i = code.find(']]>', i + 9)
                if i < 0:
                    return False
                i += 2
            elif code[i: i + 2] == '</':
                j = i + 2
                i = code.find('>', j)
                if i < 0:
                    return False
                t = code[j: i]
                if not check(t) or not stk or stk[-1] != t:
                    return False
                stk.pop()
            elif code[i] == '<':
                j = i + 1
                i = code.find('>', j)
                if i < 0:
                    return False
                t = code[j: i]
                if not check(t):
                    return False
                stk.append(t)
            i += 1
        return not stk
