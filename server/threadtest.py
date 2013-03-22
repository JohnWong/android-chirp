import threading
import datetime

class ThreadClass(threading.Thread):
    
    def run(self):
        while True:
            now = datetime.datetime.now()
            print "%s says Hello World at time: %s" % (self.getName(), now)

t = ThreadClass()
t.setDaemon(True)
t.start()
    
