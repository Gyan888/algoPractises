
from collections import Counter

class Cart:
    price={"A":[(1,50),(3,130)],"B":[(1,30),(2,45)],"C":[(1,20)],"D":[(1,15)]}

    def addToCart(self,item):
        self.totalItems=Counter(item)

    def getTotalPrice(self):      
        # in this function it is assumed that no Item can have more than one special price  
        
        total=0        
        for i in self.totalItems:
            priceChart=dict(Cart.price.get(i))
            if (self.totalItems[i])>1:                
                dicounterdNumbers=list(filter(lambda x:x>1,priceChart.keys()))
                if dicounterdNumbers:
                    quotient=self.totalItems[i]//dicounterdNumbers[0]
                    remainder=self.totalItems[i]%dicounterdNumbers[0]
                    total+=(quotient*priceChart[dicounterdNumbers[0]]+remainder*priceChart[1])
                else:
                    total+=self.totalItems[i]*priceChart[1]
            else:
                total+=priceChart.get(1,0)
        return total
    
    
    
x=Cart()
x.addToCart("AAAA")
print(x.getTotalPrice())

