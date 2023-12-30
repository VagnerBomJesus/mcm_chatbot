# README - Chatbot
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
## Descrição
O Chatbot é um programa de inteligência artificial projetado para interagir com usuários de forma automatizada, respondendo a perguntas e fornecendo assistência em um formato de conversação natural. Este README fornece informações sobre como configurar, executar e personalizar o chatbot.

## Funcionalidades

- **Respostas a Perguntas**: O chatbot pode responder a uma variedade de perguntas sobre tópicos específicos. Ele utiliza um modelo de linguagem treinado para entender e gerar respostas relevantes.

- **Comandos Personalizados**: Você pode configurar comandos personalizados que o chatbot reconhecerá e responderá de acordo.

## Pré-requisitos

Antes de usar o chatbot, certifique-se de ter instalado os seguintes componentes:

- Python 3.x
- Bibliotecas necessárias (listadas no arquivo requirements.txt)
- Um ambiente virtual é recomendado para evitar conflitos de dependências.

## Configuração

1. Clone o repositório:
   ```
   git clone https://github.com/VagnerBomJesus/mcm_chatbot.git
   ```
   
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute o chatbot:
   ```
   python chatbot.py
   ```



-------------------------------------------------





import pyttsx3

engine = pyttsx3.init()

# Listar vozes disponíveis
voices = engine.getProperty('voices')
for voice in voices:
    print("Voz:", voice.name, "Idioma:", voice.languages)

# Escolher uma voz em um idioma específico (substitua 'pt' pelo código do idioma desejado)
selected_voice = None
for voice in voices:
    if 'pt' in voice.languages[0]:
        selected_voice = voice
        break

if selected_voice:
    engine.setProperty('voice', selected_voice.id)
    engine.say("Olá, esta é uma mensagem de teste em outro idioma.")
    engine.runAndWait()
else:
    print("Voz no idioma desejado não encontrada.")


