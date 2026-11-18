class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "(" : ")" ,
            "{" : "}" ,
            "[" : "]"
        }
        tmp = []
        for char in s:
            
            if char in d.keys():
                tmp.append(char)

            elif char in d.values():
                if len(tmp) == 0:
                    return False
                
                if d[tmp[-1]] == char:
                    tmp.pop()
                else:
                    return False   
        return len(tmp) == 0
            

            

