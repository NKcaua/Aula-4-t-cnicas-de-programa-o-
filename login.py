repita = True
senha = "errada"

while repita:
    senha = input("Digite a senha: ")
if senha == "12345Python":
    print("Login bem sucedido")
    repita = False
else:
    print("Senha incorreta, digite novamente\n")