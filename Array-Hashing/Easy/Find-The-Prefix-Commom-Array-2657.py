'''

Find The Prefix Common Array - 2657

'''


def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d = dict()
        arr = []
        count = 0

        for i in range(len(A)):
            if A[i] not in d:
                d[A[i]] = 1
            else:
                d[A[i]] += 1
                count += 1
            if B[i] not in d:
                d[B[i]] = 1
            else:
                d[B[i]] += 1
                count +=1
            
            arr.append(count)
        
        return arr

'''

Can you please redo this! I dont really understand so we are goin to look at this again

'''
            