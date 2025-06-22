import base64

# Función para decodificar el video de base64 a amp4
def decode_video(coded_video: str, output_path="video.mp4"):
    try:
        #Decodificar el video de base64
        decoded_video = base64.b64decode(coded_video)

        #Guardar el video decodigicado en un archivo mp4
        with open(output_path, "wb") as video_file:
            video_file.write(decoded_video)

    except Exception as e:
        print("Error al decodificar el video:", e)