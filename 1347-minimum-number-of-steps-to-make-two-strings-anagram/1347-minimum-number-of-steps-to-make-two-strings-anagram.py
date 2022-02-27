class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        steps = 0
        for char, count in s_count.items(): 
            t_c = t_count.get(char,0)
            if t_c < count: 
                steps += count - t_c
        return steps