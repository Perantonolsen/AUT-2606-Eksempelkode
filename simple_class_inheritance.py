
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __call__(self):
        print(self.name, " is ", self.age, "years old")

class Teacher(Human):
#    def __init__(self):
#        Human.__init__(self, self.name, self.age)
    def __call__(self):
        print(self.name, " is a teacher")

if __name__ == '__main__':
    me = Teacher("Per", 29)
    me()
