from utils import load_templates, load_data, add_to_json

def index():
    note_template = load_templates('components/notes.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    
    notes = '\n'.join(notes_li)

    return  load_templates('index.html').format(notes=notes)


def submit(title, details):

    add_to_json(title, details)

