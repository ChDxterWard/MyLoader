from nicegui import ui
import requests
from dataclasses import dataclass, asdict
from RequestDto import RequestDto



def send(url, type, title):
    requestDto = RequestDto(url, type, title)
    try:
        response = requests.post(
                'http://loader_backend:8000/load/',
                json=asdict(requestDto),
                headers={'Content-Type': 'application/json'}
            )
        response.raise_for_status()
    except Exception as e:
        print(e)

def create_loader_page():
    state = {'url_str': ''}
    with ui.row().classes('w-full grid grid-cols-3 gap-4 items-center'):

        ui.element('div')
        ui.label('Your Loader').classes('text-center self-center')
        ui.element('div')

        ui.element('div')
        ui.input('Url').bind_value(state, 'url_str')
        ui.element('div')
        
        ui.element('div')
        ui.radio(['audio', 'video'], value='audio').classes('text-center self-center').props('inline').bind_value(state, 'type')
        ui.element('div')
        
        ui.element('div')
        ui.button('Load', on_click=lambda : send(state['url_str'], state['type'], state['title']))
        ui.element('div')
        
        ui.element('div')
        ui.input('Title').bind_value(state, 'title')
        ui.element('div')            

if __name__ in {'__main__', '__mp_main__'}:
    create_loader_page()
    ui.run(
        host='0.0.0.0',
        port=8080,
        reload=False,
        show=False,
        title='MyLoader'
    )