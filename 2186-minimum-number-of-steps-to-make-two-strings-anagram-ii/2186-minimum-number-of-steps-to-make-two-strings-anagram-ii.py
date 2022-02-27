class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        
        steps = 0
        for char, count in s_count.items(): 
            t_c = t_count.get(char,0)
            steps += abs(count - t_c)
        
        for char, count in t_count.items(): 
            if char in s_count: continue
            s_c = s_count.get(char,0)
            steps += abs(count - s_c)
        return steps