import json 
import dados 

def salvar_dados():
    dados_para_salvar = {
       'estoque_caixas': dados.estoque_caixas,
       'estoque_resmas': dados.estoque_resmas,
       'historico': dados.historico 
    }
    with open('dados.json', 'w') as arquivo:
       json.dump(dados_para_salvar,arquivo, indent=4)


def carregar_dados():
    try:
      with open('dados.json', 'r') as arquivo:
          dados_lidos = json.load(arquivo)

      dados.estoque_caixas = dados_lidos['estoque_caixas']
      dados.estoque_resmas = dados_lidos['estoque_resmas']
      dados.historico = dados_lidos['historico']

    except FileNotFoundError:
        print('Arquivo de dados não encontrado.')
        print('Iniciando o sistema com dados vazios!!')