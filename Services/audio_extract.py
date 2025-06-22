import subprocess

def audio_extract(video_path: str, audio_path: str):
    command = [
        "ffmpeg",
        "-i", video_path,
        "-q:a", "0",    
        "-map", "a",
        audio_path
    ]
    subprocess.run(command, check=True)