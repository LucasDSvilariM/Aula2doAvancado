# Aula2doAvancado


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

def cadastrar_usuario():
    while True:
        usuario = input("Digite o seu usuário:")
        if usuario in usuarios:
            print("Usuário cadastrado!")
        else:
            senha = input("Digite uma senha: ")
            usuarios.append(usuario)
            senhas.append(senha)
            print("cadastro feito com sucesso")

        dnv = int(input(f"Você deseja cadastrar mais um usuario?\n"
                        f"(1 - sim// 2- não: "))
        if dnv !=1:
            break


def login():
    while True:
        usuario = input("Digite o nome de usuario: ")
        senha = input("Digite sua senha: ")
        if usuario in usuarios:
            indice = usuarios.index(usuario)
            if senhas[indice] == senha:
                print(f"Bem-vindo, {usuario}!")
                break
            else:
               print("Senha incorreta!")
        else:
            print("Usuário inválido")

def mostrar():
    print("Os usuários cadastrados e suas senhas são: ")
    for x in range(len(usuarios)):
        print(f"Usuários: {usuarios[x]} e Senha: {senhas[x]}")

def saida():
    print("Encerrado")


def menu():
    while True:
        print(f"BEM VINDO!!\n"
              f"DIGITE 1 PARA REALIZAR CADASTRO\n"
              f"DIGITE 2 PARA REALIZAR LOGIN\n"
              f"DIGITE 3 PARA MOSTRAR OS USUARIOS\n"
              f"DIGITE 4 PARA SAIR \n")

        entrada = int(input("Digite a opção que deseja executar: "))
        if entrada == 1:
            cadastrar_usuario()
        elif entrada == 2:
            login()
        elif entrada == 3:
            mostrar()
        elif entrada == 4:
            print("Encerrado")
            break
        else:
            print("Inválido")
menu()
