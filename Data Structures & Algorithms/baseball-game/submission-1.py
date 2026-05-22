class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range (len(operations)) :
            n = operations[i]
            if n[0] == '-' :
                record.append(int(n))
            elif n.isnumeric() :
                record.append(int(n))
            elif n.isalpha() :
                if n == 'C' :
                    record.pop()
                else :
                    temp = int(record[-1]) * 2
                    record.append(temp)
            else :
                temp = int(record[-1]) + int(record[-2])
                record.append(temp)
            result = sum(x for x in record)
        return result 
