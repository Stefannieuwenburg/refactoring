from main import *

class Homeowner:
    def __init__(self,name,address,needs):
        self.name = name
        self.adress = address
        self.needs = needs
   
    
class Specialist:
    def __init__(self,name,proffesion):
        self.name = name
        self.proffesion = proffesion 
    super(). __init__()
    
class Electrician(Specialist):
    def __init__(self):
        self.proffesion = "Electrician"
    super(). __init__()
    
class Painter(Specialist):
    def __init__(self):
        self.proffesion = "Painter"
    super(). __init__()
    
class Plumber(Specialist):
    def __init__(self):
        self.proffesion = "Plumber"
    super(). __init__()