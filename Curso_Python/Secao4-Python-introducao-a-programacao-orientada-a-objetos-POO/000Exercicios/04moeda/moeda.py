class Moeda:
    def __init__(self, dolar, real):
        self.dolar = dolar
        self.real = real
        self.iof = 0.06
    
    
    def conversor(self):
        return f'Valor convertido para real: {(self.dolar * self.real * self.iof) + (self.dolar * self.real):.2f}'
    
