import json
import openai
import pyttsx3  # pip install pyttsx3

# carregar o datas
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


# Função para fazer o chatbot falar
def talk(texto):
    
    # Inicialização do mecanismo de fala
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 200)  # Velocidade de fala (padrão: 200, 120 = lento)
    for indice, vozes in enumerate(voices):  # Listar vozes disponíveis
        print(indice, vozes.name)
    voz = 53 #54 #53  # Escolher uma voz (índice da lista de vozes)
    engine.setProperty('voice', voices[voz].id)
    # Fala o texto usando o mecanismo de fala configurado
    engine.say(texto)
    engine.runAndWait()

