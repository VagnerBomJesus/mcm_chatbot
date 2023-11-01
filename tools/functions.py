import json
import openai
import pyttsx3  # pip install pyttsx3
import os

# Current working directory
path = os.getcwd()

# Constants
AUDIO_FILE_NAME = "audio.wav"
JSON_FILE_PATH = "tools/data/mensagens.json"


# carregar o datas
def load_messages_from_file(arquivo_json):
    try:
        with open(arquivo_json, "r") as arquivo:
            lista_mensagens = json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {arquivo_json} não encontrado. Usando lista vazia.")
        lista_mensagens = []
    except json.JSONDecodeError:
        print(
            f"Erro na decodificação do arquivo JSON {arquivo_json}. Usando lista vazia."
        )
        lista_mensagens = []
    return lista_mensagens


# Função para enviar mensagens ao Chatbot
def send_message(mensagem, lista_mensagems=[]):
    # Adicionar a mensagem do usuário à lista de mensagens
    lista_mensagems.append({"role": "user", "content": mensagem})

    # Chamar a API do OpenAI para obter uma resposta
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagems,
        max_tokens=1024,
        temperature=0.5,
    )

    # Retornar a resposta gerada pelo Chatbot
    return resposta["choices"][0]["message"]


# Função para fazer o chatbot falar
def talk(texto):
    # Inicialização do mecanismo de fala
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 200)  # Velocidade de fala (padrão: 200, 120 = lento)
    ##for indice, vozes in enumerate(voices):  # Listar vozes disponíveis
    ##print(indice, vozes.name)
    voz = 1  # 53 #54  # Escolher uma voz (índice da lista de vozes)
    engine.setProperty("voice", voices[voz].id)
    # Fala o texto usando o mecanismo de fala configurado
    engine.say(texto)
    engine.runAndWait()
    engine.stop()


def save_file(data):
    file_path = os.path.join(path, AUDIO_FILE_NAME)
    with open(file_path, "wb") as f:
        f.write(data)

def get_user_input():
    while True:
        user_input = input('Bob: Escreva aqui a sua mensagem ("sair"): ')
        if user_input == "sair":
            print("Até já, espero ter ajudado!")
            talk("Até já, espero ter ajudado!")

            return None
        yield user_input