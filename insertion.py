#insertion sort algorithm


def insertion(arr):
	for i in range(1,len(arr)):
		key=arr[i]
		j=i-1
		while (j >= 0 and key < arr[j]):
			arr[j + 1] = arr[j] 
                        j -= 1            
                arr[j+1]=key
           
    

#decorator			
import time
def decorated(fx):
	def orininal(args):
		x=time.time()
		result=fx(args)
		print("time taken ",time.time()-x)
		return result
	return orininal


def singleton(_class):
	instance={}
	def checkSingleTon(*args,**kwargs):
		if _class not in instance:
			instance[_class]=_class(*args,**kwargs)
		return instance[_class]
	return checkSingleTon

#singleton class

@singleton
class Boy:
	def __init__(self,name):
		self.name=name		
	def getName(self):
		return self.name

###singleton with metaclasses 

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# #Python2
# class MyClass(BaseClass):
#     __metaclass__ = Singleton

# #Python3
# class MyClass(BaseClass, metaclass=Singleton):
#     pass


def mergeSort(nlist):    
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0   		 #merging algorithm this will compare and merge the array in sorted way        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):            
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):            
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1


nlist = range(0,10000000)[::-1]
initialTime=time.time()
mergeSort(nlist)
print(nlist)
print ("time taken ",time.time()-initialTime)

