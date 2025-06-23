from moviepy import VideoFileClip

def audio_extract(video_path: str, audio_path: str):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    video_clip.close()