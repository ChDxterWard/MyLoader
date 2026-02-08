from nicegui import ui
import requests
from dataclasses import dataclass, asdict
from RequestDto import RequestDto



def send(url, type):
    requestDto = RequestDto(url, type)
    try:
        response = requests.post(
                'http://loader_backend:8000/load/',
                json=asdict(requestDto),
                headers={'Content-Type': 'application/json'}
            )
        response.raise_for_status()
    except Exception as e:
        print(e)
        #ui.notify(f"Error: {e}", type='negative')

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
        ui.button('Load', on_click=lambda : send(state['url_str'], state['type']))
        ui.element('div')

            

if __name__ in {'__main__', '__mp_main__'}:
    create_loader_page()
    ui.run(
        host='0.0.0.0',  # WICHTIG für Docker!
        port=8080,       # Port aus Umgebungsvariable oder fest
        reload=False,    # Für Production
        show=False
    )  
