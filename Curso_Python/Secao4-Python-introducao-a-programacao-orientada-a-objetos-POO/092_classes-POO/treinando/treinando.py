class IndoShow:
    def __init__(self, ingresso=False, locomocao=False, diversao=False):
        self.ingresso = ingresso
        self.locomocao = locomocao
        self.diversao = diversao

    def comprando_ingresso(self):
        if self.ingresso:
            print('Ingresso comprado')
            return

        print('Sem Ingresso, Sem Show.')

    def fila(self):
        if self.ingresso:
            print('Minha vez')
            self.ingresso = True
            return

        if not self.ingresso:
            print('Na fila')
            self.ingresso = True
            return

    def acabou(self):
        if self.ingresso:
            print('Acabou os ingressos')
            self.ingresso = False
            return

    def transporte(self, trans):
        if not self.locomocao:
            print(f'Vou ir pro show de {trans}.')

    def durante_show(self, foda):
        if foda == 'FODA' or 'BOM' or 'DEMAIS' or 'BOMDIMAIS':
            print(f'O show foi {foda}.')
        elif foda == 'CHATO' or 'RUIM' or 'NUNCA MAIS':
            print(f'O show foi {foda}.')

