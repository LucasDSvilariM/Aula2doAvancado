def piramide(n):
    for i in range(1,n+1):
        for x in range(i):
            print(i, end =" ")
        print()
def piramide2(n):
    for i in range(n+1):
        for x in range(1,i+1):
            print(x, end =" ")
        print()

def vogais(txt):
    cont = 0
    for x in txt:
        if x in "aeiouAEIOU":
            cont += 1
    print(f"A quantidade de vogais são: {cont}")

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
              # Encerra a função login

        if usuario in usuarios:
            indice = usuarios.index(usuario)
            for _ in range(tentativa):
                senha = input("Digite sua senha: ")
                if senhas[indice] == senha:
                    print(f"Bem-vindo, {usuario}!")

                else:
                    tentativa -= 1
                    print(f"Senha incorreta. Você tem {tentativa} tentativas restantes.")
            print("Número máximo de tentativas alcançado. Senha bloqueada.")
            senha_bloqueada = True  # Bloqueia a senha

        else:
            print("Usuário não encontrado.")


def mostrar():
    print("Os usuários cadastrados e suas senhas são: ")
    for i in range(len(usuarios)):
        print(f"Usuário: {usuarios[i]} e Senha: {senhas[i]}")

def sair():
    print("Encerrado")


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
                exit(senha_bloqueada)
        elif entrada == 3:
            mostrar()
        elif entrada == 4:
            print("Encerrado")
            exit(entrada)
        else:
            print("Opção inválida")

def atdNOVA3():
    numero = [0] * 10
    tam = len(numero)
    maior = 0
    menor = 0
    soma = 0

    for x in range(tam):
        numero[x] = int(input("Digite o número: "))

    for y in range(tam):
        if numero[y] % 2 == 0:
            print(numero[y], end=" ")
    for z in range(tam):
        if numero[z] > maior:
            maior = numero[z]
        if numero[z] < menor:
            menor = numero[z]
        soma = soma + numero[z]

    media = soma / tam
    print(media)

def inverter_nomes(nome1,nome2,nome3,nome4,nome5):
    nomes = ['']*5
    nomes[0] = nome1
    nomes[1] = nome2
    nomes[2] = nome3
    nomes[3] = nome4
    nomes[4] = nome5
    print(nomes)
    nomes.reverse()
    print(nomes)

def soma(*numeros):

    soma = 0
    n = int(input("Digite o número: "))
    tam = len(n)
    for x in range(tam):
        soma = soma + numeros[x]
    print(soma)

def texto():
    txt = "abcdefghijklmnopqrstuvxywz"
    cont = 0
    tam = len(txt)
    for x in txt:
        if x in "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVxXyYwWzZ":
            cont+=1
    print(f"O texto tem {cont} letras")

    for y in range(tam-1,-1,-1):
        print(txt[y], end =" ")