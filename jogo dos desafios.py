import getpass

print('Olá Player! Bem-vindo ao jogo!')
print()
print('___________________________________________________________________________')
print()
matprin = [['X','X','X'],['X','X','X'],['X','X','X']]
matprin1 = [['X','X','X'],['X','X','X'],['X','X','X']]
cont = -1
cont1 = -1
linhas_escolhidas = []
colunas_escolhidas = []
print('Instruções: ')
print()
print('Um player ficará responsável por criar os desafios, descrevendo um por um. ')
print('Os desafios ficarão guardados dentro do tabuleiro, porém oculto para que os outros não saibam. ')
print('Prontos, cada player vai poder escolher um desafio que deverá ser cumprido. ')
print('Quando escolhido, este não poderá ser repetido. ')
print()
print('IMPORTANTE: É proibido jogar e não se divertir! ')
print()
print('Comandos: ')
print()
print('Para "Sim" digite: 1 ')
print('Para "Não" digite: 2 ')
print()
print('___________________________________________________________________________')
resp = int(input('Deseja iniciar o jogo? \n \n'))
print()
respp = 1

# Vamos iniciar o jogo

if(resp==1):
  print()
  print('A opção escolhida foi "SIM", dessa forma: ')
  print('O jogo foi iniciado! Divirta-se! ')
  print()

# Contar as linhas e colunas

  for i in range(3):
    cont1 = cont1 + 1
    print(cont1,' ',end='')
  print()

  print("---------")
  for l in range(3):
    cont = cont + 1
    for c in range(3):
        print(matprin[l][c],' ',end='')
    print('|',cont)
  print()

# Preencher matriz
while(resp == 1):

    for l in range(3):
      print()
      print(l+1, "linha de desafio ")
      print()
      for c in range(3):
        print()
        matprin[l][c]= getpass.getpass("Digite o desafio: ")
    print('')

# Representação da Matriz Oculta

    for l in range(3):
      for c in range(3):
        print(matprin1[l][c],"|", end='')
      print()

# Escolher a Linha e Coluna
    if(respp == 1):
      print()
      linha_escolhida = int(input('Determine a linha: '))
      coluna_escolhida = int(input('Determine a coluna: '))

      if (linha_escolhida, coluna_escolhida) in zip(linhas_escolhidas, colunas_escolhidas):
        print("Essa linha e coluna já foram escolhidas. Escolha outra.")
      else:
        linhas_escolhidas.append(linha_escolhida)
        colunas_escolhidas.append(coluna_escolhida)
        valor_escolhido = matprin[linha_escolhida][coluna_escolhida]

        # Imprimindo o valor escolhido
        print(valor_escolhido)
        for i in range(8):
          resp= int(input("Você deseja escolher outro desafio? (1)SIM|(2)NÃO\n"))
          if(resp==1):
            print()
            linha_escolhida1 = int(input('Determine a linha: '))
            coluna_escolhida1 = int(input('Determine a coluna: '))
            valor_escolhido1 = matprin[linha_escolhida1][coluna_escolhida1]

            if (linha_escolhida1, coluna_escolhida1) in zip(linhas_escolhidas, colunas_escolhidas):
              print()
              print("Essa linha e coluna já foram escolhidas. Escolha outra.")
            else:
              linhas_escolhidas.append(linha_escolhida1)
              colunas_escolhidas.append(coluna_escolhida1)
              print(valor_escolhido1)
    
          else:
            print()
            print('A opção escolhida foi "NÃO", dessa forma: ')
            print()
            encerrar = int(input("Deseja encerrar o jogo? \n "))

            if(encerrar==1):
              print('O jogo foi encerrado. Agradecemos sua participação, esperamos que tenha gostado! ')
              break
            else:
              encerrar=(respp==1)

while(resp==2):
  print('A opção escolhida foi "NÃO", dessa forma: ')
  print("O jogo não será iniciado. ")
  break