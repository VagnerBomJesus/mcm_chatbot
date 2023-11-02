import openai
import speech_recognition as sr
import whisper
import time

from tools import functions

# Constants
API_KEY = "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"


def main():
    openai.api_key = API_KEY
    model = whisper.load_model("base")

    # Load messages from a JSON file using the 'functions' module
    message_list = functions.load_messages_from_file(functions.JSON_FILE_PATH)

    recognizer = sr.Recognizer()  # Create the recognizer instance outside the loop

    with sr.Microphone() as mic:
        voice_input_active = True  # Flag to track if voice input is active
        last_interaction_time = time.time()  # Initialize the last interaction time
        consecutive_unknown_errors = (
            0  # Track consecutive "sr.UnknownValueError" errors
        )

        for user_input in functions.get_user_input():
            if not user_input:
                break

            if not user_input.strip():
                continue

            if user_input.lower() == "voz":
                if not voice_input_active:
                    print("Bob: Voz ativada. Fale alguma coisa.")
                    functions.talk("Voz ativada. Fale alguma coisa.")
                    voice_input_active = True
                else:
                    print("Bob: Voz já está ativada.")
                    functions.talk("Voz já está ativada.")

            while voice_input_active:
                current_time = time.time()
                if current_time - last_interaction_time >= 30:  # 30 seconds
                    print("Bob: Saindo do reconhecimento de voz devido à inatividade.")
                    functions.talk(
                        "Saindo do reconhecimento de voz devido à inatividade."
                    )
                    voice_input_active = False
                    break

                print("Bob: Aguardando reconhecimento de voz...")
                audio = recognizer.listen(mic)
                print("Bob: Enviando para reconhecimento")

                try:
                    question = recognizer.recognize_google(audio, language="pt-BR")
                    print("Você (Voz):", question)
                    user_input = question
                except sr.UnknownValueError:
                    # valueError = "Eu não consegui entender o áudio, por favor repita."
                    # print(valueError)
                    # functions.talk(valueError)
                    # continue

                    consecutive_unknown_errors += 1
                    if consecutive_unknown_errors == 3:
                        valueError = "Será que queres me dizer alguma coisa?."
                        consecutive_unknown_errors = 0  # Reinicia o contador
                    if consecutive_unknown_errors == 2:
                        valueError = "Não consegui entender o áudio nas últimas duas tentativas, por favor repita claramente."
                    else:
                        valueError = (
                            "Eu não consegui entender o áudio, por favor repita."
                        )
                    print(valueError)
                    #functions.talk(valueError)
                    continue

                except sr.RequestError:
                    requestError = (
                        "O serviço de reconhecimento de voz do Bob não está disponível."
                    )
                    print(requestError)
                    functions.talk(requestError)
                    # continue
                    break

                if user_input.lower() == "desativar voz":
                    print("Bob: Desativando reconhecimento de voz.")
                    functions.talk("Desativando reconhecimento de voz do Bob.")
                    voice_input_active = False
                    break
                elif question == "":
                    print("No sound")
                    continue
                
                else:
                    # Obtenha a resposta do chatbot e adicione-a à lista de mensagens
                    response = functions.send_message(user_input, message_list)
                    message_list.append(response)

                    print("Bob: ", response["content"])
                    functions.talk(response["content"])
                    last_interaction_time = (
                        time.time()
                    )  # Atualiza o tempo da última interação

            # Obtenha a resposta do chatbot e adicione-a à lista de mensagens
            response = functions.send_message(user_input, message_list)
            message_list.append(response)

            print("Bob: ", response["content"])
            functions.talk(response["content"])
            last_interaction_time = time.time()  # Atualiza o tempo da última interação


if __name__ == "__main__":
    main()
