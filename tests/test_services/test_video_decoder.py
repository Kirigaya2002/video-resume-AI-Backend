import sys
import os
import base64
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Services.video_decoder import decode_video

@pytest.fixture
def sample_video():
    # Crear un video base64 de prueba
    with open("test_video.mp4", "rb") as f:
        video_bytes = f.read()
    return base64.b64encode(video_bytes).decode('ascii')

def test_decode_video(sample_video):
    # Ejecutar la función
    decode_video(sample_video)
    
    # Verificar que el archivo fue creado
    assert os.path.exists("video.mp4")
    
    # Limpiar después de la prueba
    if os.path.exists("video.mp4"):
        os.remove("video.mp4")