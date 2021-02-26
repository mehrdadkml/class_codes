# #viran khodro


class Peguet:

    __count_Pedar_object = 0  # class Attribute

    def __init__(self, color, gearbox_atumate=True, door=4):  #constructor , object method
        self.color = color
        self.gearbox_atumate = gearbox_atumate
        self.on = False
        self.door = door
        self.assign_chair()

        if self.__class__.__name__ == "Peguet":
            Peguet.__count_Pedar_object += 1

        # if self.__class__ == Peguet.__class__:
        #     Peguet.__count += 1

    def start(self):
        print("mashin roshan shod")
        self.on = True

    def booghzadan(self):
        print("booooogh")
        return "boogh zadeh shod"
    

    def __assign_chair(self, chair):
        print(f"chair {chair} add!")
    
    def assign_chair(self):
        for i in range(self.door):
            self.__assign_chair(i+1)

    # def __str__(self):
    #     return "man ye objectam"

    @classmethod
    def number_created_car(cls):
        print(cls.__count_Pedar_object)


class Peguet2Door(Peguet):



    def __init__(self, color, gearbox_atumate=True):
        self.door = 2
        super().__init__(color, gearbox_atumate, self.door)

    def start(self):
        print("barf pakon yedor becharkh")
        super().start()
        print(self.booghzadan())
    





pegeutAshkan = Peguet("abi carboni")
pegeutAshkan1 = Peguet("abi carboni")
pegeutAshkan3 = Peguet("abi carboni")

pegeutMehrnaz = Peguet2Door("sefid", False)
pegeutMehrnaz1 = Peguet2Door("sefid", False)
pegeutMehrnaz2 = Peguet2Door("sefid", False)
pegeutMehrnaz3 = Peguet2Door("sefid", False)
pegeutMehrnaz4 = Peguet2Door("sefid", False)
pegeutMehrnaz5 = Peguet2Door("sefid", False)
pegeutMehrnaz6 = Peguet2Door("sefid", False)

print(pegeutAshkan.door)
pegeutAshkan.start()
print(pegeutMehrnaz.door)
pegeutMehrnaz.start()

print(pegeutMehrnaz.number_created_car())
print(pegeutMehrnaz2.__class__.__name__)


print(pegeutMehrnaz3)






# def my_decorator(in_fun):
#     def wrapper():
#         print("before fun")

#         in_fun()

#     return wrapper


# @my_decorator
# def print_hello():
#     print("hello")

# # print_hello = my_decorator(print_hello)

# print_hello()