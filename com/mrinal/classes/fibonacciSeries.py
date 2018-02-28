from pip._vendor.distlib.compat import raw_input

class fibonacci:
    val = 0
    bal2 = 1
    
    def fibo(self,n):
        if n == 0 : 
            return 0
        elif n == 1 :
            
            return 1
        else:
            return self.fibo(n-1) + self.fibo(n-2)

    def getFibo(self, n):
        print(self.fibo(n))
        
fiboobj = fibonacci()
val = int(raw_input("Insert a new Value : "))
fiboobj.getFibo(val)
        