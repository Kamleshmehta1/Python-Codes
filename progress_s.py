from threading import Thread, Event
from time import sleep, time
from typing import TYPE_CHECKING
from tkinter import *
from tkinter.ttk import Progressbar

progress =None
event = Event()
class EVMHardwareThread(Thread):

    maxResults = 1000
    cnt = 0
    step = 1
    def __init__(self,step,maxResults):
        Thread.__init__(self)
        self.step = step
        self.maxResults = maxResults

    def run(self):
        while (self.cnt <= self.maxResults):
            self.cnt = self.cnt + self.step
            sleep(0.5)
        print('Stop Process')

    def getCnt(self):
        return self.cnt

    def getPercent(self):
        return ((self.cnt *100)/self.maxResults)

def displayVar(th1,th2,th3,root,progress) :
   
    while True:
        try:
            r=((th1.getPercent() + th2.getPercent() + th3.getPercent())/3)
           
            
            print("-----------------------------------------------------------------------")
            # print("th1 : ",th1.getPercent())
            # print("th2 : ",th2.getPercent())
            # print("th3 : ",th3.getPercent())
            # print("Avg Percent : ", ((th1.getPercent() + th2.getPercent() + th3.getPercent())/3))
            
            a=(((th1.getPercent() + th2.getPercent() + th3.getPercent())/3))
            print(type(progress))
            progress['value']= int(a)
            root.update_idletasks()
            print(a)
            sleep(1)
            
                    
        except KeyboardInterrupt:
            event.set()
            break
            

        


root=Tk()
progress=Progressbar(root,orient=HORIZONTAL,length=300,mode="determinate")
progress.place(x=50,y=50)  

my_var = [1, 2, 3]
t1 = EVMHardwareThread(10,500)
t1.start()
t2 = EVMHardwareThread(10,700)
t2.start()
t3 = EVMHardwareThread(10,1000)
t3.start()
mt = Thread(target=displayVar, args=(t1,t2,t3,root,progress ))
mt.start()

 

root.mainloop()



            

# t1.join()
# t2.join()
# t3.join()
# mt.join()
# print(my_var)



