from flask import Flask, request, render_template_string, redirect
import views

app = Flask(__name__)

NOTE_TEMPLATE = '''  
'''


app.static_folder = 'static'

# rota principal
@app.route('/')
def index():
    return render_template_string(views.index())

# rota submit
@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')

    detalhes = request.form.get('detalhes')
    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):

    views.delete_note(id)
    return redirect('/')

@app.route('/edit_page/<int:id>', methods=['GET'])
def edit_page(id):

    return render_template_string(views.edit_page(id))

@app.route('/edit_note/<int:id>', methods=['POST'])
def edit_note(id):
    
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    views.edit_note(titulo, detalhes, id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)