class PeopleFriends:

    def __init__(self,id, name, birthdate,race):
        self.id=id
        self.name = name
        self.birthdate=birthdate
        self.race=race
        self.command='No'
        
        
    def __str__(self):
        return f'|ID: {self.id} | Имя: {self.name} | Дата роэжения: {self.birthdate} | '
    
    def add_command(self,command):
        if self.command=='':
            self.command=command
        else:
            if self.command=='No':
                self.command=command
            else:
                self.command=f'{self.command}, {command}'

    def get_command(self):
        return self.command
    
       

