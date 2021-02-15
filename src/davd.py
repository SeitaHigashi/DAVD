import os
import youtube_dl

ydl = youtube_dl.YoutubeDL()

with ydl:
    result = ydl.extract_info(
        'https://youtu.be/mZ0sJQC8qkE',
        download=True 
    )
