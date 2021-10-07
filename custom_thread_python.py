import threading
from threading import Thread
from time import sleep

class myClass(Thread):
    def __init__(self,name,surname):
        Thread.__init__(self)
        self.name=name
        self.surname=surname

    def run(self):
        print("start thread")
        print(self.name,self.surname)
        print("end thread")

if __name__=="__main__":
    t1=myClass("kamlesh","mehta")
    t2=myClass("kamlesh","mehta")
    t1.start()
    sleep(0.2)
    t2.start()
    t1.join()
    t2.join()
    print("done")

