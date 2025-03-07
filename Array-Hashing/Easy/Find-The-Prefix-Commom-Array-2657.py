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
                count += 1
            if B[i] not in d:
                d[B[i]] = 1
            else:
                count +=1
            
            arr.append(count)
        
        return arr


def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()  # To track seen elements
        count = 0  # Count of common elements
        result = []  # Final array

        for i in range(len(A)):
            if A[i] in seen:  # If already seen, it's a repeat, increment count
                count += 1
            seen.add(A[i])  # Mark A[i] as seen
            
            if B[i] in seen:  # If already seen (from A or before in B), increment count
                count += 1
            seen.add(B[i])  # Mark B[i] as seen

            result.append(count)  # Store current count

        return result


'''

The way this works is that if the if index 0 of both arrays is not in the dict, you add it
but if it is, then you simply increase the count by 1. this works because there is no duplicates

'''
            