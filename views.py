from utils import load_templates, load_data, add_to_db, delete_from_db

def index():
    note_template = load_templates('components/notes.html')
    notes_li = [
        note_template.format(title=dados[0], details=dados[1], id=dados[2])
        for dados in load_data()
    ]
    
    notes = '\n'.join(notes_li)

    return  load_templates('index.html').format(notes=notes)


def submit(title, details):

    add_to_db(title, details)


def delete_note(id):

    delete_from_db(id)