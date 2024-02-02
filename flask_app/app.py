from flask import Flask, render_template

#inicializar una app con flask
app =  Flask(__name__)

# crear una ruta
# el solo poner '/' establece que es en la página ppal
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Holi crayoli {name}</h1>'




if __name__ == '__main__':
    app.run(debug = True)