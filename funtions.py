import json

def carregar_mensagens_de_arquivo(arquivo_json):
    try:
        with open(arquivo_json, "r") as arquivo:
            lista_mensagens = json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado. Usando lista vazia.")
        lista_mensagens = []
    except json.JSONDecodeError:
        print(f"Erro na decodificação do arquivo JSON {arquivo_json}. Usando lista vazia.")
        lista_mensagens = []
    return lista_mensagens
