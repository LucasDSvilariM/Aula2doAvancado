def piramide(n):
    for i in range(1,n+1):
        for x in range(i):
            print(i, end=" ")
        print()
def piramide2(n):
    for i in range(n+1):
        for x in range(1,i+1):
            print(x, end=" ")
        print()

def vogais(txt):
    cont = 0
    for x in txt:
        if x in "aeiouAEIOU":
            cont+=1
    print(f"O texto tem {cont} vogais")

usuarios = []
senhas = []
senha_bloqueada = False


def cadastrar_usuario():
    while True:
        usuario = input("Digite o seu usuário: ")
        if usuario in usuarios:
            print("Usuário já cadastrado!")
        else:
            senha = input("Digite uma senha: ")
            usuarios.append(usuario)
            senhas.append(senha)
            print("Cadastro feito com sucesso!")

        dnv = int(input("Você deseja cadastrar mais um usuário?\n(1 - sim // 2 - não): "))
        if dnv != 1:
            break


def login():
    global senha_bloqueada
    tentativa = 3
    while tentativa > 0:
        usuario = input("Digite o nome de usuário: ")

        if senha_bloqueada:
            print("A senha está bloqueada. Programa encerrado.")
            return  # Encerra a função login

        if usuario in usuarios:
            indice = usuarios.index(usuario)
            for _ in range(tentativa):
                senha = input("Digite sua senha: ")
                if senhas[indice] == senha:
                    print(f"Bem-vindo, {usuario}!")
                    return
                else:
                    tentativa -= 1
                    print(f"Senha incorreta. Você tem {tentativa} tentativas restantes.")
            print("Número máximo de tentativas alcançado. Senha bloqueada.")
            senha_bloqueada = True  # Bloqueia a senha
            return
        else:
            print("Usuário não encontrado.")
            return

def mostrar():
    print("Os usuários cadastrados e suas senhas são: ")
    for i in range(len(usuarios)):
        print(f"Usuário: {usuarios[i]} e Senha: {senhas[i]}")


def menu():
    while True:
        print(f"BEM VINDO!!\n"
              f"DIGITE 1 PARA REALIZAR CADASTRO\n"
              f"DIGITE 2 PARA REALIZAR LOGIN\n"
              f"DIGITE 3 PARA MOSTRAR OS USUÁRIOS\n"
              f"DIGITE 4 PARA SAIR\n")

        entrada = int(input("Digite a opção que deseja executar: "))
        if entrada == 1:
            cadastrar_usuario()
        elif entrada == 2:
            login()
            if senha_bloqueada:
                print("Programa encerrado.")
                break  # Encerra o loop do menu se a senha estiver bloqueada
        elif entrada == 3:
            mostrar()
        elif entrada == 4:
            print("Encerrado")
            break  # Encerra a execução do programa
        else:
            print("Opção inválida")


# Iniciar o programa

