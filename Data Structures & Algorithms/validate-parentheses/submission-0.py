class Solution:
    def isValid(self, s: str) -> bool:
        tmp = []
        for char in s:
            
            if (char == ")" or char == "]" or char == "}") and len(tmp) == 0:
                return False 


            if char == "(" or char == "[" or char == "{":
                tmp.append(char)

            elif char == ")":
                if tmp[-1] == "(":
                    tmp.pop(-1)
                else:
                    return False 
            
            elif char == "}":
                if tmp[-1] == "{":
                    tmp.pop(-1)
                else:
                    return False

            elif char == "]":
                if tmp[-1] == "[":
                    tmp.pop(-1)
                else:
                    return False
        
        return len(tmp) == 0
            

            

