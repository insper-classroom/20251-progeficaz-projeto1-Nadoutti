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

if __name__ == '__main__':
    app.run(debug=True)