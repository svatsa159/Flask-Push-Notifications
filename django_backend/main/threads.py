import threading
import os
import time
from main import notifs
def Process():
    # print(sender)
    time.sleep(10)
    os.system("convert res.jpeg -colorspace Gray res1.jpeg")
    os.system("rm res.jpeg")
    notifs.notify_users("File Processed")
class ProcessThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(ProcessThread, self).__init__(*args, **kwargs)
    
    def run(self):
        Process()


def delete():
    os.system("rm res1.jpeg")

class deleteThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(deleteThread, self).__init__(*args, **kwargs)
    
    def run(self):
        delete()