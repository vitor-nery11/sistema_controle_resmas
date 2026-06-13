from persistencia import salvar_dados,carregar_dados
import dados
import os 


def registrar_entrada():
    os.system('cls')

    quantidade_entrada = int(input('Digite a quantidade de caixas que deseja registrar:'))

    if quantidade_entrada < 0:
         print('Valor muito abaixo do esperado, tente novamente')
         return 
    
    tipo = 'entrada'

    data_entrada = input('Digite a data da entrada:')

    dados.estoque_caixas += quantidade_entrada
    dados.estoque_resmas += quantidade_entrada * 10 


    dados.historico.append({
        'tipo': tipo,
        'quantidade': quantidade_entrada,
        'data': data_entrada
    })

    salvar_dados()
    os.system('cls')
    print(f'{quantidade_entrada} caixas adicionadas com sucesso!!')
    print()
    

    

def registrar_saida():

    os.system('cls')
    quantidade_saida = int(input('Digite a quantidade que esta saindo:'))

    if quantidade_saida > dados.estoque_resmas:
         print('Saldo insuficiente para retirada!')

    
    if quantidade_saida > 10:
         print('Insira um valor menor, você pode retirar no maximo 10 resmas por saida')
         return 
         
    tipo = 'saida'

    data_saida = input('Digite a data da saida de resma:')

    setor = input('Diga qual setor esta recebendo as folhas:')

    responsavel_setor = input('Diga quem é o responsavel do setor:')

    dados.estoque_resmas -= quantidade_saida
    dados.saida_por_caixa += quantidade_saida

    dados.historico.append({
        'tipo': tipo,
        'data': data_saida,
        'quantidade': quantidade_saida,
        'setor': setor,
        'responsavel': responsavel_setor
    })

     # logica de validação de estoque 
    atualizar_estoque()

     # Persistencia de dados 
    salvar_dados()

     # alerta para validação de estoque 
    alerta_estoque()
    
    os.system('cls')
    print(f'Você retirou {quantidade_saida} resmas!')
    print(f'Estoque de resmas atual: {dados.estoque_resmas}')
    print()
  

def consultar_estoque():
        os.system('cls')
        print(f'Estoque de resma: {dados.estoque_resmas}')
        print(f'Estoque de caixas:{dados.estoque_caixas}')
        print()
        


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

# LOGICA PARA ALERTA DE ESTOQUE SOBRE QUANTIDADE DE CAIXAS
def alerta_estoque():
     if dados.estoque_caixas <= 6:
          print('Por favor faça o novo pedido de caixas e adicione no estoque!!')
     




              
             
             
        
               
               
