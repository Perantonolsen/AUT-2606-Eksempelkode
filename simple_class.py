

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __call__(self):
        print( self.name, " is ", self.age, " years old")
    def spell_name(self):
        for i in self.name:
            print(i)

if __name__ == '__main__':
    me = Human("Per",29)
    me.spell_name()
    me()
