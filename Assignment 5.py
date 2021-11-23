class funny:
    def is_divisible_by_k(self, x, k): 
        ''' 
        Checks whether x is divisible by k. 
        ''' 
        assert x%k == 0, "number can't be divisible by k"
        self.x = x
        self.k = k
        return 0
            
        
    ''' 
    Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles) 
    ''' 
    list=[]
    def addition (self, x):       
            if (self.x, 2) or (self.x, 3) or (self.x, 7):
                list.append(self.x)
                return 0
    ''' 
    Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding doubles)
    ''' 
for x in range(1,1001): 
    funny.addition(x)
    
print(funny.addition())
    



