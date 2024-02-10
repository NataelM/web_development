from flask import Flask, render_template, url_for, redirect, request

#inicializar una app con flask
app =  Flask(__name__)

# # crear una ruta
# # el solo poner '/' establece que es en la página ppal
# @app.route('/')
# def index():
#     return render_template('base.html')

# @app.route('/greet/<name>')
# def greet(name):
#     return f'<h1>Holi crayoli {name}</h1>'

# @app.route('/user/<username>/<int:age>')
# def show_user_profile(username, age):
#     return f'<h1>welcom User: {username} your age is {age}</h1>'

# @app.route('/contact')
# def contact():
#     return f'<h1> if you wanna contact me: my email is natael@.com</h1>'


####################################################
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('login.html')

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

@app.route('/submit', methods = ['POST'])
def submit():
    username = request.form['username']
    return f'Username: {username}'

if __name__ == '__main__':
    app.run(debug = True)