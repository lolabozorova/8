class Donkey(object):
 
    def __init__(self, name, maxweight, years):
        self.name = name
        self.maxweight = maxweight
        self.years = years
        
    def str(self):
        return "Donkey-boy "+ self.name + ", " + str(self.maxweight)
    def cry(self):
        return "Eeyore"*self.years
    def work_hard(self, amount):
        if amount<0:
            self.years=self.years+2
        else:
            if self.years<=amount//5:
                self.years=0
            else:
                self.years=self.years-amount//5
    
    def carry(self, load):
        if load<=self.maxweight:
            return True
        else:
            return False
    
    
    
d = Donkey('Pinoccio', 10, 5)
"""
print(d.str())
print(d.cry())
d.work_hard(16)
print(d.cry())
print(d.carry(10))
"""