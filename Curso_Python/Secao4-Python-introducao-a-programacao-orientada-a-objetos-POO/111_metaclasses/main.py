# class Meta(type):
#     def __new__(mcs, name, bases, namespace):
#         if name == 'A':
#             return type.__new__(mcs, name, bases, namespace)
#
#         if 'b_fala' not in namespace:
#             print(f'Oi, você precisa criar o metodo b_fala em {name}')
#         else:
#             if not callable(namespace['b_fala']):
#                 print(f'b_fala precisa ser um metodo, não atributo em {name}.')
#         return type.__new__(mcs, name, bases, namespace)


# class A(metaclass=Meta):
#     def fala(self):
#         self.b_fala()
#
#
# class B(A):
#     def b_fala(self):
#         print('oi')
#
#
# b = B()

#  Outro codigo com esse codigo apaga o codigo que ia rescrever o codigo

# class Meta(type):
#     def __new__(mcs, name, bases, namespace):
#         if name == 'A':
#             return type.__new__(mcs, name, bases, namespace)
#         if 'attr_classe' in namespace:
#             print(f'{name} tentou sobrescrever o atributo.')
#             del namespace['attr_classe']
#         return type.__new__(mcs, name, bases, namespace)
#
#
# class A(metaclass=Meta):
#     attr_classe = 'Valor A'
#
#
# class B(A):
#     attr_classe = 'Valor B'
#
#
# class C(B):
#     attr_classe = 'Valor C'
#
#
# b = B()
# print(b.attr_classe)

# Jeito mais abreviado de fazer
class Pai:
    nome = 'teste'


A = type('A', (Pai, ), {'attr': 'Olá Mundo!'})
a = A()
print(a.attr)
print(type(a.nome))