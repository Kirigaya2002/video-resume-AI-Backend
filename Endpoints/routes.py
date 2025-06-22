from flask import Blueprint, jsonify
from Services import *
from Services import resume_audio
from Services import video_decoder

routes = Blueprint("routes", __name__)


@routes.get("/process-video")
def process_video(Video: str):
    # Pasar video de base 64 a mp4
    video_decoder.decode_video(Video)
    # Extraer audio del video
    audio_text = ""
    # Transcribir audio a texto
    transcription = transcript_audio.transcript_audio()
    # Resumir texto obtenido
    resumed_text = resume_audio.resume_audio(transcription)
    # crear un json con la transcripcion y el resumen
    json_res = {"transcription": transcription, "resumed_text": resumed_text}
    return jsonify(json_res)
