# README - Chatbot

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



   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



   (vm_python) pi@raspberrypi:~/Desktop/mcm_chatbot $ aplay -L
null
    Discard all samples (playback) or generate zero samples (capture)
jack
    JACK Audio Connection Kit
pulse
    PulseAudio Sound Server
default:CARD=sndrpigooglevoi
    snd_rpi_googlevoicehat_soundcar, Google voiceHAT SoundCard HiFi voicehat-codec-0
    Default Audio Device
sysdefault:CARD=sndrpigooglevoi
    snd_rpi_googlevoicehat_soundcar, Google voiceHAT SoundCard HiFi voicehat-codec-0
    Default Audio Device
dmix:CARD=sndrpigooglevoi,DEV=0
    snd_rpi_googlevoicehat_soundcar, Google voiceHAT SoundCard HiFi voicehat-codec-0
    Direct sample mixing device
dsnoop:CARD=sndrpigooglevoi,DEV=0
    snd_rpi_googlevoicehat_soundcar, Google voiceHAT SoundCard HiFi voicehat-codec-0
    Direct sample snooping device
hw:CARD=sndrpigooglevoi,DEV=0
    snd_rpi_googlevoicehat_soundcar, Google voiceHAT SoundCard HiFi voicehat-codec-0
    Direct hardware device without any conversions
plughw:CARD=sndrpigooglevoi,DEV=0
    snd_rpi_googlevoicehat_soundcar, Google voiceHAT SoundCard HiFi voicehat-codec-0
    Hardware device with all software conversions
usbstream:CARD=sndrpigooglevoi
    snd_rpi_googlevoicehat_soundcar
    USB Stream Output



---------------------------------



import pyttsx3

# Inicialize o mecanismo pyttsx3 com o driver identificado
engine = pyttsx3.init(driverName='snd_rpi_googlevoicehat_soundcar')

# Realize um teste para verificar se o driver está funcionando
engine.say("Olá, esta é uma mensagem de teste.")
engine.runAndWait()
