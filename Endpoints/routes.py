from flask import Blueprint
from Services import *
from Services import resume_audio

routes = Blueprint('routes', __name__)

@routes.get('/process-video')
def process_video(Video: str):
    # Pasar video de base 64 a mp4

    #Extraer audio del video
    
    #Transcribir audio a texto

    #Resumir texto obtenido
    return resume_audio.resume_audio()