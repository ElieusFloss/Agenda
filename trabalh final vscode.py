class agenda():
    Data = ""
    Hora = None
    Duração = float
    Descrição = ""

# opcao 1 = Inserindo informacoes
def inserir(ag):
    ag.data = input("Digite a data do  seucompromisso\n")
    ag.data.hora = input("Digite a hora de seu compromisso\n")
    ag.data.hora.duracao = input("Digite a duracao do seu comprisso\n")
    ag.data.hora.descricao = input("Digite uma descricao para seu compromisso\n")
    return ag



#opcao 2 consulta por data ou hora
def consultar(vetor):
  while True:
    print("|------------------------------------------------|")
    print("| Selecione a data que deseja consultar:         |")
    print("|                                                |")
    print("|------------------------------------------------|")
    opcao = input("Digite a opcao que deseja")
    




# Opcao 3 alterar algo no compromisso





# Opcao 4 excluir compromisso da agenda
def deletarCompromisso(vetor, data):
  if len(vetor) != 0:
    for i in range(len(vetor)):
      if(vetor[i].data==data):
        vetor.pop(i)
        print("Compromisso removido!")
        break




# lopcao 5 listando os itens
def listar(vetor):
    for i in range(len(vetor)):
        print("\n\n|------------------------------------------|")
        print(f"\n|  Data do compromisso:      {vetor[i].data}     ""|")               
        print(f"\n|  Hora do compromisso:      {vetor[i].hora}        ""|")
        print(f"\n|  Duracaocao do compromisso {vetor[i].duracao}          ""|")                       
        print(f"\n|  Descricao do Compromisso: {vetor[i].descricao}         ""|")                    
        print("|------------------------------------------|")
        print("\n")
        print("\n")
        print("\n")








vetor = []
# menu opcoes
while True:

    print("|                MENU DE OPCOES              |")
    print("|============================================|")
    print("|    Opcao 1 - Inserir                       |")
    print("|    Opcao 2 - Consultar                     |")
    print("|    Opcao 3 - Alterar                       |")
    print("|    Opcao 4 - Excluir                       |")
    print("|    Opcao 5 - Listar todos                  |")
    print("|    Opcao 6 - Sair                          |")
    print("|============================================|")
    print("\n")
    op = int(input("|  Digite a opcao desejada               "))

    if op == 1:
        ag = agenda()
        vetor.append(inserir(ag))
    elif op == 2:
        print("Consultar")
    elif op == 3:
       print("Alterar")
    elif op == 4:
        data = input("Digite a data do compromisso que deseja excluir")
        deletarCompromisso(vetor, data)
    elif op == 5:
        listar(vetor)
    elif op == 6:
        print("Sair")
    else:
        print("\n\n\n")
        print('|-------------------------------|')
        print('|     Opcao Digitada inválida   |')
        print('| Voce será direcionado ao menu |')
        print('|                               |')
        print('|                               |')
        print('|  Favor Digitar uma das opcoes |')
        print('|            validas            |')
        print('|-------------------------------|')
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")

