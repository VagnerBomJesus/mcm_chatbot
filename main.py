import openai
from tools import funtions

def main():
    # Nome do arquivo JSON que contém as mensagens
    arquivo_json = "tools/data/mensagens.json"
    
    # Inicialização da Chave da API
    openai.api_key = "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"

    # Carregar mensagens do arquivo JSON usando a função do módulo funtions
    lista_mensagems = funtions.carregar_mensagens_de_arquivo(arquivo_json)

    # Loop de Conversa
    while True:
        # Entrada do Usuário
        texto = input('Eu sou o Bob como Posso ajudar ("sair"): ')

        # Verificação de Saída
        if texto == "sair":
            sair = "Até já, espero ter ajudado!"
            print(sair)
            funtions.talk(sair)
            break
        else:
            # Obter a resposta do Chatbot e adicionar à lista de mensagens
            resposta = funtions.envir_mensagem(texto, lista_mensagems)
            lista_mensagems.append(resposta)

            print("Chatbot:", resposta["content"])
            funtions.talk(resposta["content"])

if __name__ == "__main__":
    main()

