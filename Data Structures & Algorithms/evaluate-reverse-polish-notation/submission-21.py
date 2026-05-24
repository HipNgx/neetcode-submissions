class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tempList = []
        for i in range(len(tokens)) :
            n = tokens[i]
            if n.isdigit() or (n[0] == '-' and len(n) > 1) :
                tempList.append(int(n))
                print(tempList)
            else:
                if n == '+':
                    m = tempList[-1] + tempList[-2]
                elif n == '-':
                    m = tempList[-2] - tempList[-1]
                elif n == '*':
                    m = tempList[-1] * tempList[-2]
                else:
                    m = int(tempList[-2] / tempList[-1])  # ✅ truncate
                tempList.pop()
                tempList.pop()
                tempList.append(m)
        return tempList[-1]