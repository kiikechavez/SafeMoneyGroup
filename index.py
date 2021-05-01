from flask import Flask, render_template


PORT = 8080
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home2.html')

@app.route('/cursos')
def cursos():
    return render_template('curso.html')

@app.route('/nosotros')
def nosotros():
    return render_template('quienes.html')

@app.route('/inscribete')
def inscribete():
    return render_template('inscribete.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=PORT)