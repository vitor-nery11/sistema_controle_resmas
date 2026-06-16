from persistencia import salvar_dados,carregar_dados
from datetime import datetime
import dados
import os 

# FUNÇÃO PARA ENTRADA DE DADOS NO SISTEMA COM VALIDAÇÃO DE ERRROS FEITA
def registrar_entrada():
    os.system('cls')

    while True:
       try:
          quantidade_entrada = int(input('Digite a quantidade de caixas que deseja registrar:'))

          if quantidade_entrada <= 0:
               print('Digite uma entrada mais alta,tente novamente')
               continue
          break
       
       except ValueError:
            print('Digite apenas numeros')


    if quantidade_entrada < 0:
         print('Valor muito abaixo do esperado, tente novamente')
         return 
    
    tipo = 'entrada'

    data = input('Digite a data da entrada:')

    validar_data(data)

    dados.estoque_caixas += quantidade_entrada
    dados.estoque_resmas += quantidade_entrada * 10 


    dados.historico.append({
        'tipo': tipo,
        'quantidade': quantidade_entrada,
        'data': data
    })

    salvar_dados()
    os.system('cls')
    print(f'{quantidade_entrada} caixas adicionadas com sucesso!!')
    print()
    
# FUNÇÃO PARA SAIDA DE DADOS NO SISTEMA COM VALIDAÇÃO DE ERROS FEITA 
def registrar_saida():

    os.system('cls')

    while True:
          try:
               quantidade_saida = int(input('Digite a quantidade que esta saindo:'))

               if quantidade_saida <= 0 :
                    print('Quantidade precisa ser maior do que zero') 
                    continue
           

               if quantidade_saida > dados.estoque_resmas:
                    print('Saldo insuficiente para retirada!')
                    continue 

    
               if quantidade_saida > 10:
                    print('Insira um valor menor, você pode retirar no maximo 10 resmas por saida')
                    continue
           
               break

          except ValueError:
               print('Valor invalido, tente novamente')


    while True: 
          data = input('Digite a data da saida de resma:').strip()

          validar_data(data)
          break


    while True:
          setor = input('Diga qual setor esta recebendo as folhas:').strip()

          if setor.strip() == '':
               print('ops, parece que você não digitou nada, por favor tente novamente')
               continue
          break


    while True: 
          responsavel_setor = input('Diga quem é o responsavel do setor:').strip()

          if responsavel_setor == '':
                print('Campo obrigatorio, tente novamente')
                continue 
          
          break


    tipo = 'saida'

    dados.estoque_resmas -= quantidade_saida
    dados.saida_por_caixa += quantidade_saida

    dados.historico.append({
        'tipo': tipo,
        'data': data,
        'quantidade': quantidade_saida,
        'setor': setor,
        'responsavel': responsavel_setor
    })

     # logica de validação de estoque 
    atualizar_estoque()

     # Persistencia de dados 
    salvar_dados()

    
    os.system('cls')
  
    print(f'Você retirou {quantidade_saida} resmas!')
    print(f'Estoque de resmas atual: {dados.estoque_resmas}')
    alerta_estoque()
    print()
  
# FUNÇÃO PARA CONSULTAR DADOS NO ESTOQUE
def consultar_estoque():
        os.system('cls')
        print(f'Estoque de resma: {dados.estoque_resmas}')
        print(f'Estoque de caixas:{dados.estoque_caixas}')
        print()
        
# FUNÇÃO PARA MOSTRAR HISTORICO DE DADOS
def mostrar_historico():
     os.system('cls')
     print('=== HISTORICO ===')
     for movimentacoes in dados.historico:
          
          if movimentacoes['tipo'] == 'entrada':
               print('ENTRADA:')
               print(f'Data: {movimentacoes['data']}')
               print(f'Quantidade: {movimentacoes['quantidade']}')
               print('--------------------')
               print()
               
               
          
          if movimentacoes['tipo'] == 'saida':
               print('SAIDA')
               print(f'Data: {movimentacoes['data']}')
               print(f'Quantidade: {movimentacoes['quantidade']}')
               print(f'Setor: {movimentacoes['setor']}')
               print(f'Responsavel: {movimentacoes['responsavel']}')
               print('---------------------')
               print()

# FUNÇÃO PARA GERAR RELATORIO DE DADOS DO SISTEMA 
def gerar_relatorio():
     os.system('cls')
     print('======= RELATORIO =======')
     print()
     print(f'Estoque atual de caixas {dados.estoque_caixas}')
     print(f'Estoque de atual de resmas {dados.estoque_resmas}')

     total_entrada = 0
     total_saida = 0
     total_movimentações = len(dados.historico)

     # logica para definir quantidade de entradas e saidas na função
     for movimentacao in dados.historico:
        if movimentacao['tipo'] == 'entrada':
             total_entrada += 1
        elif movimentacao['tipo'] == 'saida':
             total_saida += 1 
             
        
     print(f'Total de entradas: {total_entrada}')

     print(f'Total de saidas:{total_saida}')

     print(f'Total de movimentações:{total_movimentações}')
     print()

# LOGICA PARA VALIDAÇÃO DE ESTOQUE DE CAIXAS BASEADO NO GASTO DE RESMAS
def atualizar_estoque():
     if dados.saida_por_caixa == 10:
          dados.estoque_caixas -= 1
          dados.saida_por_caixa -= 10

# LOGICA PARA ALERTA DE ESTOQUE SOBRE QUANTIDADE DE CAIXAS
def alerta_estoque():
     if dados.estoque_resmas <= 60:
          print('Por favor faça o novo pedido de caixas e adicione no estoque!!')

# LOGICA PARA FILTRAR MOVIMENTAÇÕES PELA DATA 
def filtrar_data():
     print('Escolha a opção que deseja filtrar:')
     print('1. Entrada')
     print('2. Saida')
     print()
     escolha_filtro = int(input('Escolha uma opção:'))
     data_filtrada = []

     if escolha_filtro == 1:
           data_selecionada = input('Digite a data que deseja filtrar:')
           for movimentacao in dados.historico:
               if movimentacao['tipo'] == 'entrada' and movimentacao['data'] == data_selecionada:
                    data_filtrada.append(movimentacao)
               
     if escolha_filtro == 2:
          data_selecionada = input('Digite a data que deseja filtrar:')
          for movimentacao in dados.historico:
               if movimentacao['tipo'] == 'saida' and movimentacao['data'] == data_selecionada:
                    data_filtrada.append(movimentacao)
                

     os.system('cls')
     print('======= HISTÓRICO FILTRADO =======')

     for movimentacao in data_filtrada:

          print(f"Tipo: {movimentacao['tipo']}")
          print(f"Data: {movimentacao['data']}")
          print(f"Quantidade: {movimentacao['quantidade']}")

          if movimentacao['tipo'] == 'saida':
                print(f"Setor: {movimentacao['setor']}")
                print(f"Responsável: {movimentacao['responsavel']}")

          print('-' * 30)
          print()

# FUNÇÃO PARA VALIDAR AS DATA RECEBIDAS PELOS USUARIOS
def validar_data(data):
     try:
          # validação de tamanho
          if len(data) != 10:
             print('tente novamente, sua data parece ter um tamanho inadequado')
             return False

          # validação de data
          data_valida = datetime.strptime(data, '%d/%m/%Y')
          if data_valida == True:
               return data_valida
          
     except ValueError: 
          print('Houve um erro, tente novamente')



     

     

     





              
             
             
        
               
               
