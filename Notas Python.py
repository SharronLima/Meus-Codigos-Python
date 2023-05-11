#         Notas De Escola

# Usando try para para trocar as mensagens de erro para o usuário
try:
# Declarando a variável
    pontos = float(input("Digite sua nota: "))
# Declarando as condições
    if pontos >= 6 and pontos <= 10:
        print("Aprovado.")
    elif pontos < 6:
        print("Reprovado.")
    elif pontos > 10:
        print("Número invalido.")
# Declarando exeções  
except ValueError:
    print("Resposta invalida, por favor tente novamente.")
