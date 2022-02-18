class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def binSum(a,b,c):
            l = [a,b,c]
            if l.count(1) == 3: return 1,1
            if l.count(1) == 2: return 0,1
            if l.count(1) == 1: return 1,0
            return 0,0
        
        def sum_binary(ind,carry,summation):
            if ind == len(a)+1:
                if carry: return str(carry)
                return ''
                
            s,c = binSum(int(a[-ind]), int(b[-ind]), carry)
            return sum_binary(ind+1, c, summation) + str(s)
        
        if len(a) > len(b): 
            b = ('0' * (len(a)-len(b))) + b
        if len(a) < len(b): 
            a = ('0' * (len(b)-len(a))) + a
        return sum_binary(1,0,'')
            
        