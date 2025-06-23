import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Services.audio_extract import audio_extract

def test_audio_extraction():
    # Necesitarás un video de prueba para esta prueba
    test_video = "test_video.mp4"
    test_audio = "test_audio.mp3"
    
    # Ejecutar la función
    audio_extract(test_video, test_audio)
    
    # Verificar que el archivo de audio fue creado
    assert os.path.exists(test_audio)