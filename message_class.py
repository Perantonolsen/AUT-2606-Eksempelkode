class Message():
    def __init__(self,tekst):
        self.tekst = tekst
    def __call__(self):
        print(self.tekst)
    def bokstav1(self):
        print(self.tekst[0])
    def __add__(self, string):
        self.tekst += string
    def __sizeof__(self):
        return len(self.tekst)

class Message_child(Message):
    def __init__(self,tekst):
        Message.__init__(self,tekst)
        #super().__init__(tekst)
    def __call__(self):
        print(self.tekst, " ", len(self.tekst))


if __name__ == "__main__":
    M = Message("hei")
    print(M.__sizeof__())
    M2 = Message_child("hallo")
    M2()
