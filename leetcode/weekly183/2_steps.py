class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s) 
        
        def add1(s):
            if len(s) == 0:
                s.append('1')
                return
            if s[-1] == '0':
                s[-1] = '1'
                return
            c = s.pop()
            add1(s)
            s.append('0')
        
        steps = 0
        while len(s) > 1:
            if s[-1] == '1':
                add1(s)
            else:
                s.pop()
            steps += 1
            
        return steps
    
