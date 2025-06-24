# Video Resume AI Backend

🎥 **Backend API para procesamiento inteligente de videos con transcripción y resumen automático**

## 📋 Descripción del Proyecto

Video Resume AI Backend es una API REST desarrollada en Flask que proporciona servicios de procesamiento de video utilizando inteligencia artificial. El sistema permite:

- **Decodificación de videos**: Convierte videos codificados en base64 a formato MP4
- **Extracción de audio**: Extrae la pista de audio de los videos
- **Transcripción automática**: Utiliza OpenAI Whisper para convertir el audio a texto
- **Resumen inteligente**: Genera resúmenes detallados del contenido transcrito usando Groq AI

### ✨ Características Principales

- 🔄 Procesamiento de videos en formato base64
- 🎵 Extracción automática de audio de videos
- 🗣️ Transcripción de audio a texto con alta precisión
- 📝 Generación de resúmenes inteligentes
- 🌐 API REST con soporte CORS
- 🧪 Suite de pruebas unitarias incluida

## 🏗️ Arquitectura del Proyecto

```
video-resume-AI-Backend/
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── Endpoints/             
│   └── routes.py          # Definición de rutas de la API
├── Services/              # Lógica de negocio
│   ├── video_decoder.py   # Decodificación de videos base64
│   ├── audio_extract.py   # Extracción de audio
│   ├── transcript_audio.py # Transcripción con Whisper
│   └── resume_audio.py    # Resumen con Groq AI
└── tests/                 # Pruebas unitarias
    ├── test_endpoints/
    └── test_services/
```

## 🚀 Instalación en Windows

### Prerrequisitos

- **Python 3.8+** - [Descargar desde python.org](https://www.python.org/downloads/)
- **Git** - [Descargar desde git-scm.com](https://git-scm.com/download/win)
- **FFmpeg** - [Descargar desde ffmpeg.org](https://ffmpeg.org/download.html)

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/video-resume-AI-Backend.git
cd video-resume-AI-Backend
```

### Paso 2: Crear entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
API_KEY=tu_groq_api_key_aqui
```

> **Nota**: Obtén tu API key de Groq desde [console.groq.com](https://console.groq.com)

### Paso 5: Ejecutar la aplicación

```bash
python main.py
```

La API estará disponible en `http://localhost:5000`

## 📡 Uso de la API

### Endpoint Principal

**POST** `/process-video`

Procesa un video codificado en base64 y retorna la transcripción y resumen.

#### Request Body

```json
{
  "Video": "data:video/mp4;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEA..."
}
```

#### Response

```json
{
  "transcription": "Texto completo de la transcripción del audio...",
  "resumed_text": "Resumen inteligente del contenido transcrito..."
}
```

### Ejemplo de uso con curl

```bash
curl -X POST http://localhost:5000/process-video \
  -H "Content-Type: application/json" \
  -d '{
    "Video": "tu_video_en_base64_aqui"
  }'
```

## 🧪 Ejecutar Pruebas

```bash
# Ejecutar todas las pruebas
python -m pytest tests/

# Ejecutar pruebas con cobertura
python -m pytest tests/ --cov=Services --cov=Endpoints
```

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito |
|------------|-----------|
| **Flask** | Framework web para la API REST |
| **OpenAI Whisper** | Transcripción de audio a texto |
| **Groq AI** | Generación de resúmenes inteligentes |
| **MoviePy** | Procesamiento de video y extracción de audio |
| **Flask-CORS** | Manejo de CORS para requests cross-origin |

## 🔧 Configuración Avanzada

### Variables de Entorno

| Variable | Descripción | Requerido |
|----------|-------------|-----------|
| `API_KEY` | Clave de API de Groq | ✅ |

### Modelos de Whisper Disponibles

- `tiny` - Más rápido, menos preciso
- `base` - Balance entre velocidad y precisión
- `small` - Buena precisión, velocidad moderada
- `medium` - Alta precisión, más lento
- `large` - Máxima precisión, más lento
- `turbo` - **Predeterminado** - Balance óptimo
- **Versión**: 1.0.0
- **Estado**: En desarrollo activo

---

*Desarrollado con ❤️ para el procesamiento inteligente de contenido de video*
