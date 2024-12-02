#ler entrada do usuario
nome = input() #armazenar o nome do aluno
n1 = float(input()) # 4 notas do aluno
n2 = float(input())
n3 = float(input())
n4 = float(input())
faltas = int(input())
#calculo da média
media = (n1+n2+n3+n4)/4
# logica da situação
if faltas > 31:
    situacao = "reprovado por falta"
elif media >= 8:
    situacao = "aprovado"
elif media >= 5: #recuperação
    recuperacao = float(input())#ler a nota da prova de recuperação
    if recuperacao >= (10-media):
     situacao = "aprovado na recuperação"
    else:
     situacao = "reprovado na recuperação"
else:
   situacao = "reprovado por média"
#relatorio
print("nome:",nome)
print("notas:",n1,n2,n3,n4)
print("faltas:",faltas)
print("media:",media)
print("situacao:",situacao)

