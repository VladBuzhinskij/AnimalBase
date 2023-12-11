from PeopleFriends import PeopleFriends

class HomeAnimals (PeopleFriends):
    
    def __init__(self,id,name,birthdate,race):
        super().__init__(id,name,birthdate,race)
       
    def __str__(self):
        return f'\n{super().__str__()}|Семейство: {self.race}|' 