import sys
import os
import pytest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Endpoints import routes
from flask import Flask

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(routes.routes)
    app.config['TESTING'] = True
    return app.test_client()

@patch('Endpoints.routes.video_decoder.decode_video')
@patch('Endpoints.routes.audio_extract.audio_extract')
@patch('Endpoints.routes.transcript_audio.transcript_audio')
@patch('Endpoints.routes.resume_audio.resume_audio')
def test_process_video(mock_resume, mock_transcript, mock_audio, mock_decode, client):
    # Configurar mocks
    mock_transcript.return_value = "test transcription"
    mock_resume.return_value = "test summary"
    
    # Ejecutar prueba
    response = client.post('/process-video', 
                          json={"Video": "test_video_base64"})
    
    # Verificar resultados
    assert response.status_code == 200
    assert response.json == {
        "transcription": "test transcription",
        "resumed_text": "test summary"
    }