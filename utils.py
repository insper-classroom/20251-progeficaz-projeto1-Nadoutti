import json

def load_data(file_path):
    with open(f"static/data/{file_path}", 'r') as f:
        response = json.load(f)
        return response

def load_templates(file_path):
    with open(f"static/templates/{file_path}", "r") as f:
        response = f.read()
        return response

def add_to_json(title, details):
    new_data = {
        'titulo': title,
        'detalhes': details
    }
    with open('static/data/notes.json', 'r') as file:
        
        data = json.load(file)
    
    data.append(new_data)

    with open('static/data/notes.json', 'w') as file:

        json.dump(data, file)
     