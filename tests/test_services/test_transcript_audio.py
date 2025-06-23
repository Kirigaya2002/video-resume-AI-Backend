import sys
import os
import pytest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Services.transcript_audio import transcript_audio

@patch('Services.transcript_audio.whisper.load_model')
def test_transcript_audio(mock_load_model):
    mock_model = MagicMock()
    mock_model.transcribe.return_value = {"text": "TRANSCRIPCIÓN DE PRUEBA"}
    mock_load_model.return_value = mock_model
    
    result = transcript_audio()
    assert "Don Pollo" in result  # Verificamos parte del texto esperado