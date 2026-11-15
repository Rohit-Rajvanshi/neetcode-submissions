class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r_max = arr[-1]
        arr[-1] = -1
        for i in range (len(arr)-2 , -1 , -1):
            original = arr[i]
            arr[i] = r_max 
            r_max = max(r_max , original)
        return arr 


            

    


        
        