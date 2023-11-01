#TODO: Este código Python implementa um chatbot simples que utiliza o modelo de linguagem GPT-3.5-turbo da OpenAI para responder às mensagens dos usuários em uma conversa interativa com memória.

# Importação da Biblioteca OpenAI
import openai

# Inicialização da Chave da API
openai.api_key = "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"

# Função para enviar mensagens ao Chatbot
def envir_mensagem(mensagem, lista_mensagems=[]):
    # Adicionar a mensagem do usuário à lista de mensagens
    lista_mensagems.append({"role": "user", "content": mensagem})

    # Chamar a API do OpenAI para obter uma resposta
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=lista_mensagems
    )

    # Retornar a resposta gerada pelo Chatbot
    return resposta["choices"][0]["message"]

# Inicialização da lista de mensagens
lista_mensagems = []
# Eu posso adicionar uma mesnagem inicial para o chat 
#lista_mensagems = [{"role": "system", "content": "Apartide de agora você é um assistente gente boa. E meu nome é ChatBJ, desenvolvida pelo BJ Tech!"}]

# Loop de Conversa
while True:
    # Entrada do Usuário
    texto = input('Escreva aqui a sua mensagem ("sair"): ')

    # Verificação de Saída
    if texto == "sair":
        print("Até já, espero ter ajudado!")
        break
    else:
        # Obter a resposta do Chatbot e adicionar à lista de mensagens
        resposta = envir_mensagem(texto, lista_mensagems)
        lista_mensagems.append(resposta)
        print("Chatbot:", resposta["content"])
