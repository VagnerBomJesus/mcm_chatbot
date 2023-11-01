import openai
import speech_recognition as sr
import whisper

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
        for user_input in functions.get_user_input():
            if not user_input:
                break

            if not user_input.strip():
                continue

            if user_input.lower() == "voz":
                print("Fale alguma coisa")
                audio = recognizer.listen(mic)
                print("Enviando para reconhecimento")

                try:
                    question = recognizer.recognize_google(audio, language="pt-BR")
                    print("Me: ", question)
                    user_input = question
                except sr.UnknownValueError:
                    valueError = "Bob: Não consegui entender o áudio, podes repetir por favor."
                    print(valueError)
                    functions.talk(valueError)

                    continue
                except sr.RequestError:
                    requestError = "Bob: O serviço de reconhecimento de voz não está disponível."
                    print(requestError)
                    functions.talk(requestError)
                    continue

            # Get the response from the chatbot and add it to the message list
            response = functions.send_message(user_input, message_list)
            message_list.append(response)

            print("Bob: ", response["content"])
            functions.talk(response["content"])

if __name__ == "__main__":
    main()
