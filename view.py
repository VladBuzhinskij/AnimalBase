from PackAnimals import PackAnimals
from Shelter import Shelter
from counter import Counter
shelter=Shelter()
counter=Counter()


def type_animal():
    inp=input("Выберити тип животного:\n1. Домашнее \n2. Въючное\n")
    match inp:
        case "1":
            race=import_hrace()
            shelter.add_h_animals(import_ha(),race)
        case "2":
            race=import_prace()
            shelter.add_p_animals(import_hp(),race)

def import_ha():
    hA=["кличку", "дату рождения"]
    res=list()
    for i in hA:
        print("1")
        inp=input(f"Введите {i}")
        res.append(inp)
        if inp=="":
            raise Exception('not all fields are filled in')

    return res


def import_hp():
    hp=["кличку", "дату рождения","вес"]
    res=list()
    for i in hp:
        inp=input(f"Введите {i}")
        res.append(inp)
        if inp=="":
            raise Exception('not all fields are filled in')
    return res


def import_hrace():
    inp=input("Выберите номер семейства:\n1. Кошки\n2. Собаки\n3. Хомяки\n")
    match inp:
        case "1":
            inp="Кошки"
        case "2":
            inp="Собаки"
        case "3":
            inp="Хомяки"
    return inp


def import_prace():
    inp=input("Выберите номер семейства:\n1.Лошади\n2. Ослы\n3. Верблюды\n")
    match inp:
        case "1":
            inp="Лошади"
        case "2":
            inp="Ослы"
        case "3":
            inp="Верблюды"
    return inp


def print_sheltor():
    lis=shelter.out_seheltor()
    for i in lis:
        print (i)


start=True
while start:
    inp=input("1. Завести новое животное\n2. Список команд\n3. Добавить команду\n4. Список животных\n5. Выход\nВведите номер пункта:\n")
    match inp:
        case "1":
            type_animal()
        case "2":
            print_sheltor()
            inp=input("Введите ID животного:\n")
            while not(inp.isdigit()):
                inp=input("Введите ID животного:\n")
            id=-1
            for i in shelter.out_seheltor():
                if i.id==int(inp):
                    print(i.get_command())
                    id=1
            if id<0:
                print("Животное с таким ID не найдено")
        case "3":
            print_sheltor()
            inp=input("Введите ID животного:\n")
            while not(inp.isdigit()):
                inp=input("Введите ID животного:\n")
            id=-1
            for i in shelter.out_seheltor():
                if i.id==int(inp):
                    inp2=input("Введите команду для добавления:/n")
                    print(i.add_command(inp2))
                    id=1
            if id<0:
                print("Животное с таким ID не найдено")
        case "4":
            print_sheltor()
        case "5":
            start=False



