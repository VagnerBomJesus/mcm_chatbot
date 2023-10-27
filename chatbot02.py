#TODO: Este código Python implementa um chatbot simples que utiliza o modelo de linguagem GPT-3.5-turbo da OpenAI para responder às mensagens dos usuários em uma conversa interativa com memória com o agrecimo de voz na resposta.

# Importação da Biblioteca OpenAI
import openai

import pyttsx3  # pip install pyttsx3

# Inicialização da Chave da API
openai.api_key = "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"

# Inicialização do mecanismo de fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)  # Velocidade de fala (padrão: 200, 120 = lento)
for indice, vozes in enumerate(voices):  # Listar vozes disponíveis
    print(indice, vozes.name)
voz = 1  # Escolher uma voz (índice da lista de vozes)
engine.setProperty('voice', voices[voz].id)

# Função para fazer o chatbot falar
def talk(texto):
    # Fala o texto usando o mecanismo de fala configurado
    engine.say(texto)
    engine.runAndWait()
    engine.stop()

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
# lista_mensagems = []
# Você pode adicionar uma mensagem inicial para o chatbot, como uma apresentação
lista_mensagems = [{"role": "system", "content": "A partir de agora você está interagindo com o ChatBJ, um assistente amigável desenvolvido pela BJ Tech!"}]

# Loop de Conversa
while True:
    # Entrada do Usuário
    texto = input('Escreva aqui a sua mensagem ("sair"): ')

    # Verificação de Saída
    if texto == "sair":
        sair = "Até já, espero ter ajudado!"
        print(sair)
        talk(sair)
        break
    else:
        # Obter a resposta do Chatbot e adicionar à lista de mensagens
        resposta = envir_mensagem(texto, lista_mensagems)
        lista_mensagems.append(resposta)

        print("Chatbot:", resposta["content"])
        talk(resposta["content"])
