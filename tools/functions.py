import json
import openai
import pyttsx3
import speech_recognition as sr

# Inicialização da Chave da API
openai.api_key = "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"

# Estados do Chatbot
ESTADO_AGUARDANDO = 1
ESTADO_ATIVO = 2
ESTADO_INPUT_TERMINAL = 3

# Idiomas
IDIOMA_PORTUGUES = 'pt-PT'
IDIOMA_INGLES = 'en-US'
idioma_atual = IDIOMA_PORTUGUES

# IDs das vozes para cada idioma (substitua pelos valores corretos)
VOZ_PORTUGUES = 54
VOZ_INGLES = 11

JSON_FILE_PATH = "tools/data/mensagens.json"

def load_messages_from_file(arquivo_json):
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

def enviar_mensagem(mensagem, lista_mensagens):
    lista_mensagens.append({"role": "user", "content": mensagem})
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=lista_mensagens
    )
    return resposta.choices[0]["message"]

def falar(texto):
    global idioma_atual, VOZ_PORTUGUES, VOZ_INGLES
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 130)

    if idioma_atual == IDIOMA_PORTUGUES:
        voz_selecionada = VOZ_PORTUGUES
    else:
        voz_selecionada = VOZ_INGLES

    engine.setProperty("voice", voz_selecionada)
    engine.say(texto)
    engine.runAndWait()

def obter_entrada_por_voz():
    global idioma_atual
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Aguardando o comando de voz...")
        audio = recognizer.listen(mic)
    try:
        return recognizer.recognize_google(audio, language=idioma_atual)
    except sr.UnknownValueError:
        return "Desculpe, não consegui entender o que você disse."
    except sr.RequestError:
        return "Erro no serviço de voz."

def aguardar_comando_de_ativacao():
    while True:
        texto = obter_entrada_por_voz()
        print(f"Você disse: {texto}")
        if "bob" in texto.lower():
            return

def main():
    global idioma_atual
    estado = ESTADO_AGUARDANDO
    lista_mensagens = load_messages_from_file(JSON_FILE_PATH)

    while True:
        if estado == ESTADO_AGUARDANDO:
            print("Aguardando ativação por voz...")
            texto = obter_entrada_por_voz()
            print(f"Você disse: {texto}")
            if "bob" in texto.lower():
                estado = ESTADO_ATIVO
                print("Bob ativado. Como posso ajudar?")
                falar("Bob ativado. Como posso ajudar?")

        elif estado == ESTADO_ATIVO:
            print("Você pode falar agora:")
            texto = obter_entrada_por_voz()
            print(f"Você disse: {texto}")

            if "obrigado" in texto.lower():
                estado = ESTADO_AGUARDANDO
                print("Bob desativado. Aguardando novo comando.")
                falar("Bob desativado. Aguardando novo comando.")
                continue

            if "terminal" in texto.lower():
                estado = ESTADO_INPUT_TERMINAL
                print("Bob: Mudando para input pelo terminal.")
                falar("Mudando para input pelo terminal.")
                continue

            if "mudar para inglês" in texto.lower():
                idioma_atual = IDIOMA_INGLES
                print("Bob: Mudando para inglês.")
                falar("Mudando para inglês.")
                continue

            if "mudar para português" in texto.lower():
                idioma_atual = IDIOMA_PORTUGUES
                print("Bob: Mudando para português.")
                falar("Mudando para português.")
                continue

            if texto.lower() == "sair":
                resposta_final = "Até já, espero ter ajudado!"
                print("Bob:", resposta_final)
                falar(resposta_final)
                break

            resposta = enviar_mensagem(texto, lista_mensagens)
            lista_mensagens.append({"role": "assistant", "content": resposta["content"]})
            print("Bob:", resposta["content"])
            falar(resposta["content"])

        elif estado == ESTADO_INPUT_TERMINAL:
            texto = input("Você (Terminal): ")

            if texto.lower() == "voz":
                estado = ESTADO_ATIVO
                print("Bob: Mudando para reconhecimento de voz.")
                falar("Mudando para reconhecimento de voz.")
                continue
           
            if "mudar para inglês" in texto.lower():
                idioma_atual = IDIOMA_INGLES
                print("Bob: Mudando para inglês.")
                falar("Mudando para inglês.")
                continue

            if "mudar para português" in texto.lower():
                idioma_atual = IDIOMA_PORTUGUES
                print("Bob: Mudando para português.")
                falar("Mudando para português.")
                continue

            if texto.lower() == "sair":
                resposta_final = "Até já, espero ter ajudado!"
                print("Bob:", resposta_final)
                falar(resposta_final)
                break

            resposta = enviar_mensagem(texto, lista_mensagens)
            lista_mensagens.append({"role": "assistant", "content": resposta["content"]})
            print("Bob:", resposta["content"])
            falar(resposta["content"])

if __name__ == "__main__":
    main()
