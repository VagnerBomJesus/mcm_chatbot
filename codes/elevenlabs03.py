import json
import openai
import pyttsx3
import speech_recognition as sr
from elevenlabs import generate, play, voices, set_api_key, User, Voice, VoiceSettings

# Inicialização da Chave da API
openai.api_key = "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"
elevenlabs_api_key = "6197176b683e266ef8224debc2dfbc9b"

# Estados do Chatbot
ESTADO_AGUARDANDO, ESTADO_ATIVO, ESTADO_INPUT_TERMINAL = 1, 2, 3

# Idiomas
IDIOMA_PORTUGUES, IDIOMA_INGLES = 'pt-PT', 'en-US'
idioma_atual = IDIOMA_PORTUGUES

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

def generate_speech(text, voice_name="Paul"):
    set_api_key(elevenlabs_api_key)
    user = User.from_api()
    restantes = user.subscription.character_limit - user.subscription.character_count
    print("Restantes:", restantes, "Total:", user.subscription.character_limit)

    caracteres_total = len(''.join(text))
    print("Total de caracteres", caracteres_total)

    if restantes < caracteres_total:
        print("Não há créditos suficientes.")
        return

    # Selecionar a voz
    available_voices = voices()
    selected_voice = next((v.voice_id for v in available_voices if voice_name in v.name), None)

    if not selected_voice:
        print(f"Voz '{voice_name}' não encontrada.")
        return

    # Gerar o áudio
    audio = generate(
        text=text,
        voice=Voice(voice_id=selected_voice,
                    settings=VoiceSettings(stability=0.35,
                                           similarity_boost=0.4,
                                           style=0.55,
                                           use_speaker_boost=True)),
        model='eleven_multilingual_v2'
    )

    # Reproduzir o áudio
    try:
        play(audio)
    except ValueError as e:
        print(f"Erro ao reproduzir o áudio: {e}")
def obter_entrada_por_voz():
    r = sr.Recognizer()

    # Usar o microfone como fonte de áudio
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconhecendo...")

        # Reconhecimento de voz usando o Google Speech Recognition
        texto = r.recognize_google(audio, language="pt-PT")
        print(texto)

    except Exception as e:
        print("Não foi possível solicitar resultados do serviço Google Speech Recognition; {0}".format(e))
        return "None"

    return texto
        


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
                generate_speech("Bob ativado. Como posso ajudar?", voice_name="Paul")

        elif estado == ESTADO_ATIVO:
            print("Você pode falar agora:")
            texto = obter_entrada_por_voz()
            print(f"Você disse: {texto}")

            if "obrigado" in texto.lower():
                estado = ESTADO_AGUARDANDO
                print("Bob desativado. Aguardando novo comando.")
                generate_speech("Bob desativado. Aguardando novo comando.", voice_name="Paul")
                continue

            if "terminal" in texto.lower():
                estado = ESTADO_INPUT_TERMINAL
                print("Bob: Mudando para input pelo terminal.")
                generate_speech("Mudando para input pelo terminal.", voice_name="Paul")
                continue

            if "mudar para inglês" in texto.lower():
                idioma_atual = IDIOMA_INGLES
                print("Bob: Mudando para inglês.")
                generate_speech("Mudando para inglês.", voice_name="Paul")
                continue

            if "mudar para português" in texto.lower():
                idioma_atual = IDIOMA_PORTUGUES
                print("Bob: Mudando para português.")
                generate_speech("Mudando para português.", voice_name="Paul")
                continue

            if texto.lower() == "sair":
                resposta_final = "Até já, espero ter ajudado!"
                print("Bob:", resposta_final)
                generate_speech(resposta_final, voice_name="Paul")
                break

            resposta = enviar_mensagem(texto, lista_mensagens)
            lista_mensagens.append({"role": "assistant", "content": resposta["content"]})
            print("Bob:", resposta["content"])
            generate_speech(resposta["content"], voice_name="Paul")

        elif estado == ESTADO_INPUT_TERMINAL:
            texto = input("Você (Terminal): ")

            if texto.lower() == "voz":
                estado = ESTADO_ATIVO
                print("Bob: Mudando para reconhecimento de voz.")
                generate_speech("Mudando para reconhecimento de voz.", voice_name="Paul")
                continue

            if texto.lower() == "sair":
                resposta_final = "Até já, espero ter ajudado!"
                print("Bob:", resposta_final)
                generate_speech(resposta_final, voice_name="Paul")
                break

            resposta = enviar_mensagem(texto, lista_mensagens)
            lista_mensagens.append({"role": "assistant", "content": resposta["content"]})
            print("Bob:", resposta["content"])
            generate_speech(resposta["content"], voice_name="Paul")

if __name__ == "__main__":
    main()
