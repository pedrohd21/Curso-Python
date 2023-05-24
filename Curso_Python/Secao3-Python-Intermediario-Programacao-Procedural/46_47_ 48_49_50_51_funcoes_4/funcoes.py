variavel = 'Valor'


def func():
    print(variavel)


def func2():
    # global variavel // nn é boa pratica de programação
    variavel = 'Outro valor'
    print(variavel)


func()
func2()
