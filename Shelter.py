from HomeAnimals import HomeAnimals
from PackAnimals import PackAnimals

class Shelter:
    id=0
    def __init__(self):
        self.shelter=[]

    def add_h_animals(self,animal,typ):
        self.shelter.append(HomeAnimals(self.id,animal[0],animal[1],typ))
        self.id=self.id+1

    def add_p_animals(self,animal,typ):
        self.shelter.append(PackAnimals(self.id,animal[0],animal[1],animal[2],typ))
        self.id=self.id+1
        
    def out_seheltor(self):
        return self.shelter
            