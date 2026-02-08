from fastapi import FastAPI
import yt_dlp
import os
from RequestDto import RequestDto
import traceback
from fastapi import HTTPException

app = FastAPI()

path_to_ffmpeg = '/usr/bin/ffmpeg'

def download(url: str, type: str, output_path: str = '/out', noplaylist=True):
    ydl_opts = {
        'format': 'best' if type == 'video' else 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': False,
        'noplaylist': noplaylist,
        'js_runtimes': {
            'nodejs': {
                'path': '/usr/bin/node'
            }
        },
    }
    
    if type == 'audio':
        ydl_opts.update({
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'postprocessor_args': ['-ar', '44100'],
        })
    elif type == 'video':
        ydl_opts.update({
            'merge_output_format': 'mp4',
        })
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        error_details = traceback.format_exc()
        print(f"Download error: {error_details}")
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/")
async def root():
    return {"message": "Hello World"}

@app.post("/load")
async def receive_data(data: RequestDto):
    download(data.url, 'audio')
    return {"message": f"URL received: {data.url, data.type}"}