import dados

def registrar_entrada():
    tipo = 'entrada'

    quantidade_entrada = int(input('Digite a quantidade de caixas que deseja registrar:'))

    data_entrada = input('Digite a data da entrada:')

    dados.estoque_caixas += quantidade_entrada
    dados.estoque_resmas += quantidade_entrada * 10 

    dados.historico.append({
        'tipo': tipo,
        'quantidade': quantidade_entrada,
        'data': data_entrada
    })

    print(f'{quantidade_entrada} caixas adicionadas com sucesso!!')

    

def registrar_saida():

    quantidade_saida = int(input('Digite a quantidade que esta saindo:'))

    if quantidade_saida > dados.estoque_resmas:
         print('Saldo insuficiente para retirada!')
         return 
         
    tipo = 'saida'

    data_saida = input('Digite a data da saida de resma:')

    setor = input('Diga qual setor esta recebendo as folhas:')

    responsavel_setor = input('Diga quem é o responsavel do setor:')

    dados.estoque_resmas -= quantidade_saida

    dados.historico.append({
        'tipo': tipo,
        'data': data_saida,
        'quantidade de resmas': quantidade_saida,
        'setor': setor,
        'responsavel': responsavel_setor
    })

    print(f'Você retirou {quantidade_saida} resmas!')
    print(dados.estoque_resmas)
  

def consultar_estoque():
        print(f'Estoque de resma: {dados.estoque_resmas}')
        print(f'Estoque de caixas:{dados.estoque_caixas}')



def mostrar_historico():
     for movimentacoes in dados.historico:
          print(movimentacoes)