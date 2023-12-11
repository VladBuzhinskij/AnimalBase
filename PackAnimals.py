from PeopleFriends import PeopleFriends

class PackAnimals (PeopleFriends):
    def __init__(self,id,name,birthdate,weight,race):
        super().__init__(id,name,birthdate,race)
        
        self.weight=weight
    def __str__(self):
        return f'\n{super().__str__()} | Вес: {self.weight} | Семейство: {self.race} |' 
