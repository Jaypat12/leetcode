def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        Occur = 1
        d=dict()
        arr = []
 
        #holds dict with all different occurance of x
        for i in range(len(nums)):
            if nums[i] == x:
                d[Occur] = i
                Occur += 1

        print(d)
        
        for q in queries:
            if q in d:
                arr.append(d[q])
            else:
                arr.append(-1)
        
        return arr

'''

finish

'''