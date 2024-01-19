# README - Chatbot
# ../../Desktop/virtualenv/bin/activate
# ELEVEN LABS
- 6197176b683e266ef8224debc2dfbc9b
- 5961ea0afb983651c3229cc643582dcb
- b4584b915b7a3e4cc70ec5483af577fa
#
 username = "biomimicry"
    password = "biomimicry"
    cluster_name = "cluster0.y0qr26c"
    dbname = "biomimicryBDR"
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
``````
sudo apt-get install flac
``````
## Este comando instalará o utilitário de linha de comando FLAC, que é usado pela biblioteca speech_recognition para converter o áudio gravado para o formato FLAC antes de enviá-lo para o serviço de reconhecimento de voz do Google.



```
pip install pyaudio
```
## Se você encontrar problemas ao instalar o pyaudio diretamente com pip, pode ser necessário instalar algumas dependências do sistema primeiro. 

````
sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio
````
## Depois de instalar as dependências, tente instalar o pyaudio novamente com pip. Se ainda assim encontrar dificuldades, pode ser necessário buscar soluções específicas para a instalação do pyaudio no Raspberry Pi, pois às vezes a instalação pode variar dependendo da configuração do hardware e do sistema operacional.


````
sudo apt-get install espeak

````
## Este comando instalará o espeak e suas dependências no seu Raspberry Pi.
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


