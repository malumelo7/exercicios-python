class Piloto:
    cor: str
    fechado: bool
    texto: str

    def __init__(self,cor, fechado=True):
        self.cor = cor
        self.fechado = fechado

    def escrever(self):
        print(texto)
    
    def abrir(self):
        if self.fechado:
            print(f'O piloto {self.cor} está fechado')
        if not self.fechado:
            self.fechado = False
            print(f'O piloto {self.cor} está aberto')



piloto1 = Piloto('Preto')

texto = 'Estou escrevento aaa'
piloto1.escrever()
piloto1.abrir()