class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t : return False
        
        s_ind, t_ind = 0,0 
        s_len, t_len = len(s) , len(t)
        
        while s_ind < s_len and t_ind < t_len: 
            
            if s[s_ind] == t[t_ind]: 
                s_ind += 1
                
            t_ind += 1
            
        return  s_ind == s_len 
            
            
        
        