from gtts import gTTS


def text_to_speech(text, language="en"):
    try:
        tts = gTTS(text=text, lang=language)

        file_path = "response.mp3"

        tts.save(file_path)

        return file_path

    except Exception as e:
        print("Audio generation failed:", e)

        return None