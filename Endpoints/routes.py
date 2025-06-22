from flask import Blueprint
from Services import *
from Services import resume_audio

routes = Blueprint('routes', __name__)


@routes.get('/process-video')
def process_video(Video: str):
    # Pasar video de base 64 a mp4
    video_path = "";
    #Extraer audio del video
    audio_text = "";
    #Transcribir audio a texto
    transcription = "";
    #Resumir texto obtenido
    return resume_audio.resume_audio(transcription)