class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 :
            return False
        opened = ['(', '[','{']
        closed = [')', ']', '}']
        completed = ['()', '[]', '{}']
        if s[0] in closed :
            return False
        cur = []
        for i in s :
            if i in opened : 
                cur.append(i)
            else :
                if len(cur) != 0 :
                    m = cur.pop()
                    temp = m + i
                    if temp not in completed :
                        return False
        if len(cur) > 0 :
            return False
        return True  