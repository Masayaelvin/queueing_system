from datetime import datetime 
from queue import Queue


class queue:
    '''defines what will be happening in a queue'''
    
    
    def __init__(self):
        self.__queue_list = []
        self.__queue_count = 0
        
    def join(self,name):
        self.joined_at = datetime.now().strftime("%H"":""%M"":""%S"" ""year:-""%Y")
        self.__queue_list.append(name)
        self.__queue_count += 1
        print(f"{name} you are currently at position {self.__queue_count} in the list")
    
    def check_queue(self):
        return len(self.__queue_list) == 0
    2
    def queue_list(self):
        if self.check_queue():
            print("The queue is empty")
            return
        print("The queue list is:")
        count = 0
        for name in self.__queue_list:
            count += 1 
            print(f"position:{count} name: {name}")

    def position(self,name):
        if name in self.__queue_list:
            return print(f"{name} you are currently at position\
 {self.__queue_list.index(name)+1} in the list")
        else:
            return print(f"{name} you are not in the queue")
        
    
    def leave(self):
        leave = []
        if self.check_queue():
            print("The queue is empty")
            return
        self.__queue_count -= 1
        left_at = datetime.now().strftime("%H"":""%M"":""%S"" ""year:-""%Y")
        print(self.__queue_list[0])
        self.__queue_list.pop(0)
        data = {"name":self.__queue_list[0],"joined_at":self.joined_at,"left_at":left_at}
        leave.append(data)
        print(f"you have left the queue at {left_at}")
        return leave

