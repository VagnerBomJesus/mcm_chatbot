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



-------------------------------------------------
import pyttsx3

engine = pyttsx3.init(driverName='snd_rpi_googlevoicehat_soundcar')

erro (vm_python) pi@raspberrypi:~/Desktop/mcm_chatbot $ python main.py
Traceback (most recent call last):
  File "/home/pi/Desktop/vm_python/lib/python3.7/site-packages/pyttsx3/__init__.py", line 20, in init
    eng = _activeEngines[driverName]
  File "/usr/lib/python3.7/weakref.py", line 137, in __getitem__
    o = self.data[key]()
KeyError: 'snd_rpi_googlevoicehat_soundcar'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "main.py", line 3, in <module>
    engine = pyttsx3.init(driverName='snd_rpi_googlevoicehat_soundcar')
  File "/home/pi/Desktop/vm_python/lib/python3.7/site-packages/pyttsx3/__init__.py", line 22, in init
    eng = Engine(driverName, debug)
  File "/home/pi/Desktop/vm_python/lib/python3.7/site-packages/pyttsx3/engine.py", line 30, in __init__
    self.proxy = driver.DriverProxy(weakref.proxy(self), driverName, debug)
  File "/home/pi/Desktop/vm_python/lib/python3.7/site-packages/pyttsx3/driver.py", line 50, in __init__
    self._module = importlib.import_module(name)
  File "/usr/lib/python3.7/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 965, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'pyttsx3.drivers.snd_rpi_googlevoicehat_soundcar'

