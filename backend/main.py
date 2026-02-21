from fastapi import FastAPI
import yt_dlp
from RequestDto import RequestDto
import traceback
from fastapi import HTTPException

app = FastAPI()

path_to_ffmpeg = '/usr/bin/ffmpeg'

def download(url: str, type: str, title: str = '', output_path: str = '/out', no_playlist=True):
    output_url = f'{output_path}/{title}' if title else f'{output_path}/%(title)s.%(ext)s'
    ydl_opts = {
        'format': 'best' if type == 'video' else 'bestaudio/best',
        'outtmpl': output_url,
        'quiet': False,
        'no_warnings': False,
        'noplaylist': no_playlist,
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
        print(f'Download error: {error_details}')
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/load')
async def receive_data(data: RequestDto):
    download(data.url, data.type, data.title)
    return {'message': f'URL received: {data.url, data.type}'}