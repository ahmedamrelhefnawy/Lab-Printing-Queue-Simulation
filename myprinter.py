class printer:
    def __init__(self,pages):
        self.pagerate = pages
        self.currenttask = None
        self.timeremaining = 0
    
    def tick(self):
        if self.currenttask != None:
            self.timeremaining -= 1
            if self.timeremaining == 0:
                self.currenttask = None
    
    def busy(self):
        if self.currenttask != None:
            return True
        else:
            return False
        
    def startnext(self,newtask):
        self.currenttask = newtask
        self.timeremaining = newtask.getpages() * 60 / self.pagerate