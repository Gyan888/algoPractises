import socket
from queue import Queue
import threading

q=Queue()
lock=threading.Lock()
target='blackbelthelp.com'

def outsource(job):
    k=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        con=k.connect((target,job))
        with lock:
            print('port ',job ,'is open')#lock feature is not gonna let any other thread access this resource until the
                                         #current thread is done with it       
            con.close()
    except:
        pass
            

def work():
    while True:
        job=q.get()
        outsource(job)
        q.task_done()

for jobs in range(100):
    q.put(jobs)
    
for workers in range(50):
    s=threading.Thread(target=work)
    s.start()
    
q.join()

