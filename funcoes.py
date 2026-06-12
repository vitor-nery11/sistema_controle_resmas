import dados

def registrar_entrada():
    tipo = 'entrada'

    quantidade_entrada = int(input('Digite a quantidade de caixas que deseja registrar:'))

    data_entrada = input('Digite a data da entrada')

    dados.estoque += quantidade_entrada

    dados.historico.append({
        'tipo': tipo,
        'quantidade': quantidade_entrada,
        'data': data_entrada
    })

    print(dados.estoque)

    

def registrar_saida():
    data_saida = input('Digite a data da saida de resma')

    quantidade_saida = int(input('Digite a quantidade que esta saindo:'))

    setor = input('Diga qual setor esta recebendo as folhas')

    responsavel_setor = input('Diga quem é o responsavel do setor:')
  

def consultar_estoque():
    print(dados.estoque)