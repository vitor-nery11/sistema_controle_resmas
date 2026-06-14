from funcoes import registrar_entrada, registrar_saida, consultar_estoque, mostrar_historico,gerar_relatorio, filtrar_data
from persistencia import carregar_dados

print('Seja bem vindo ao sistema de controle de resmas')

# Mecanismo de persistencia de dados: Utilizando json para carregar os dados salvos
carregar_dados()
print()

while True:
  print('1. registrar entrada de resmas')
  print('2. registrar saida de resmas')
  print('3. consultar estoque de resmas')
  print('4. consultar historico')
  print('5. Gerar relatorio')
  print('6. filtrar por data')
  print('7. sair')

  opcoes_validas = 1,2,3,4,5,6,7

  while True:
    try: 
      escolha = int(input('Digite a sua escolha:'))
 
      if escolha not in opcoes_validas:
         print('O valor digitado não esta em nosso menu, tente novamente')
         continue
    
      break

    except ValueError:
       print('Digite apenas numeros:')
     
     
     
     

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
     filtrar_data()
    
  elif escolha == 7:
      print('Encerrando sistema!!')
      break

  