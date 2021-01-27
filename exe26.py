class Jarra:
    jarra:int
    volume:int

    def __init__(self,jarra=0):
        self.jarra = jarra

    def encher(self, volume):
        self.jarra += volume

    def esvazia(self,volume):
        self.jarra -= volume
        if self.jarra < 0:
            self.jarra = 0
        else:
            self.jarra


    def analisa(self):
        print(f'A jarra tem {self.jarra} litros')

jarra = Jarra()

jarra.encher(5)
jarra.encher(8)
jarra.esvazia(14)
jarra.analisa()