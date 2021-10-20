#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# – Quantidade de notas                                                                                                                                                  
# – A maior nota                                                                                                                                                                
# – A menor nota                                                                                                                                                              
# – A média da turma                                                                                                                                                      
# – A situação (opcional)

def notas(*notas, situacao = True):

    def soma():
        soma = 0
        for v in notas:
            soma += v
        return soma

    dict = {}
    dict["Quantidade de Notas"] = len(notas)
    dict["Maior Nota"] = max(notas)
    dict["Menor Nota"] = min(notas)
    dict["Média da Turma"] = (soma() / len(notas))
    if situacao:
        if dict["Média da Turma"] < 7:
            dict["Situação da turma"] = 'FUDEU BAHIA'
        else:
            dict["Situação da turma"] = 'Alright'
    return dict



print(notas(5,6,2,7,1,8,7))




