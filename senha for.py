#   Senhas usando o For

print("Bem vindo, Por favor digite sua senha.")

# loop para 3 tentativas
for s in range(3):
    senha = input("Digite sua senha: ")
    if senha != "sharron":
        print("Senha incorreta.")
    # se caso a senha for a correta, encerre o loop
    if senha == "sharron":
        print("Valido.")
        break
print("Fim")
