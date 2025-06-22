from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("API_KEY"))


def resume_audio(text: str):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Vas a actuar como un asistente que resume textos con gran detalle en caso de que sea un texto extenso, "
                + "sin importar la longitud de esta, no pongas palabras ni texto fuera de un resumen, "
                + "quiero que tu respuesta solo sea el resumen del texto brindado. Texto: "
                + text,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return response.choices[0].message.content
