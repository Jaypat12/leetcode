def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        Occur = 1
        d=dict()
        arr = []
 
        #holds dict with all different occurance of x
        for i in range(len(nums)):
            if nums[i] == x:
                d[Occur] = i
                Occur += 1
        
        for q in queries:
            if q in d:
                arr.append(d[q])
            else:
                arr.append(-1)
        
        return arr

'''

The function occurrencesOfElement identifies the index positions of a given number x in a list 
(nums) based on the occurrence count. It first builds a dictionary (d) where the keys represent
the occurrence number of x, and the values store the corresponding index positions in nums. Then,
 for each query in queries, it checks if the requested occurrence exists in d. If it does, the 
 function returns the stored index; otherwise, it returns -1, indicating that x appears fewer 
 times than requested. This approach efficiently maps occurrences of x and allows quick retrieval 
 of their positions.

'''