

from elevenlabs import generate, play, voices, set_api_key, User, Voice, VoiceSettings

def generate_speech(text, voice_name="Paul", stability=0.35, similarity_boost=0.4, style=0.55, boost=False, falar=True, api_key="89927a3b616612fa3dda68c6d44dffa7"):
    set_api_key(api_key)

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
                    settings=VoiceSettings(stability=stability,
                                           similarity_boost=similarity_boost,
                                           style=style,
                                           use_speaker_boost=boost)),
        model='eleven_multilingual_v2'
    )

    # Reproduzir o áudio
    if falar:
        try:
            play(audio)
        except ValueError as e:
            print(f"Erro ao reproduzir o áudio: {e}")

def main():
    texto = "Olá, eu sou o Bob. Seja bem-vindo, Vagner!"
    # A voz escolhida agora é "Paul" por padrão
    generate_speech(texto, falar=True)

if __name__ == "__main__":
    main()

