class Solution:
    def fib(self, n: int) -> int:
        
        
        if n < 2: return n
        
        res = [0] * (n+1)
        
        def fibo(n):
            
            if n < 2 : return n
            
            res[n] = fibo(n-1) + fibo(n-2)
            return res[n]
        
        fibo(n)
        return res[n]
        