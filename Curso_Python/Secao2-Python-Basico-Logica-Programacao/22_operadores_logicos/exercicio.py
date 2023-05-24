usuario = str(input('Nome do usuário: '))
senha = str(input('Senha do usuário: '))
usuario_vd = 'Pedro'
senha_vd = '123456'
if usuario_vd == usuario and senha_vd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha invalidos.')