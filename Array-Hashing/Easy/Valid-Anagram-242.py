'''

Valid Anagram 242

'''


def isAnagram(self, s: str, t: str) -> bool:
        
        d=dict()

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in t:
            if i not in d:
                return False
            else:
                d[i] -= 1

        for i in s:
            if d[i] != 0:
                return False
            
        return True

'''

The idea was to take the first word and place it into a hashmap. So that
each letter would have a freqency. Then with the next word, I would go through
each letter in that and see if that letter exists in the hashmap, if it does not, 
I return False because both words should have the same letters. If it does exits in 
hashmap, I subtract 1 from the frequcnyt of that letter. The idea is that at the end
of it each letter should have the same frequency, hence why I check if each letter
has a frequency of 0. Finally if all of those are met, i can return True.

'''