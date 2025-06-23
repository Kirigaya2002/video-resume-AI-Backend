import sys
import os
import pytest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from Services.resume_audio import resume_audio

@patch('Services.resume_audio.Groq')
@patch('Services.resume_audio.load_dotenv')
def test_resume_audio(mock_load_dotenv, mock_groq):
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="MOCKED RESPONSE"))]
    mock_client.chat.completions.create.return_value = mock_response
    mock_groq.return_value = mock_client
    
    result = resume_audio("test text")
    assert isinstance(result, str)  # Solo verificamos que devuelva un string