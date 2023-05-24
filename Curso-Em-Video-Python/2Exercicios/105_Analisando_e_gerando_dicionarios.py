def notas(* valores, sit=False):
    """
    -> função para analisar notas e varias situações dos alunos
    :param valores: Uma ou mais nota de alunos, aceita quantas quiser
    :param sit: retorna se o ano foi bom ou ruim do aluno
    :return: dicionario com varios informações dos alunos
    """
    dic = dict()
    dic['total'] = len(valores)
    dic['maior'] = max(valores)
    dic['menor'] = min(valores)
    dic['media'] = sum(valores) / len(valores)
    if sit:
        if dic['media'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['media'] >= 5:
            dic['situação'] = 'RAZOAVEL'
        else:
            dic['situação'] = 'RUIM'
    return dic


resp = notas(10, 9, 8, sit=True)
print(resp)
help(notas)