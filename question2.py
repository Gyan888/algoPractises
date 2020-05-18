seatNames={0: 'a', 1: 'b', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 2: 'c'}

class AirBus:
    Seats={1:8*[0],2:8*[0],3:8*[0]}    
    Order={
        4:[(2,5),(0,1),(6,7)],
        3:[(2,4)],
        2:[(0,1),(6,7)],
        1:[(0,7)]
    }                
    def allocateSeat(self,Number):
        bookedSeat=[]
        isSeatBooked=False      
        RemainedToBook=Number         
        if AirBus.Order.get(Number,False):
            availableOrder=AirBus.Order.get(Number)            
            for row in AirBus.Seats:
                for i,j in availableOrder:                    
                    if (1 not in AirBus.Seats[row][i:j+1] or Number is 1 ) and not isSeatBooked:                                                
                        for k in range(i,j+1):
                            if AirBus.Seats[row][k]!=1 and RemainedToBook!=0:                                
                                AirBus.Seats[row][k]=1
                                bookedSeat.append(str(row)+seatNames.get(k))                                                                                                            
                                RemainedToBook-=1                                            
                                isSeatBooked=True if len(bookedSeat)==Number  else ""                                                                
        else:
            return "No AirBus.Seats can be booked with given Number"
        print ("Seat Booked are ",bookedSeat)      
        
a=AirBus()
a.allocateSeat(4)
a.allocateSeat(3)
a.allocateSeat(3)
a.allocateSeat(2)
a.allocateSeat(2)
a.allocateSeat(4)
a.allocateSeat(1)
print(a.Seats)