class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tmp = []

        for i in operations:  
            if i == "+":
                tmp.append(tmp[-1] + tmp[-2])
            elif i == "C":
                tmp.pop(-1)

            elif i == "D":
                v = tmp[-1]
                tmp.append(v*2)
            else:
                tmp.append(int(i))

        return sum(tmp)