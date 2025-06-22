import whisper

model = whisper.load_model("turbo")

def transcript_audio():
    #Cargar audio
    audio = whisper.load_audio("audio.mp3")

    #Transcribir el audio
    result = model.transcribe(audio)

    return result["text"]