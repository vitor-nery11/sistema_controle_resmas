from funcoes import registrar_entrada, registrar_saida, consultar_estoque, mostrar_historico,gerar_relatorio

print('Seja bem vindo ao sistema de controle de resmas')

while True:
  print('1. registrar entrada de resmas')
  print('2. registrar saida de resmas')
  print('3. consultar estoque de resmas')
  print('4. consultar historico')
  print('5. Gerar relatorio')
  print('6. sair')

  escolha = int(input('Digite a sua escolha:'))

  if escolha == 1:
    registrar_entrada()

  elif escolha == 2:
    registrar_saida()

  elif escolha == 3: 
    consultar_estoque()

  elif escolha == 4:
    mostrar_historico()

  elif escolha == 5:
      gerar_relatorio()
    
  elif escolha == 6:
      print('Encerrando sistema!!')
      break

  