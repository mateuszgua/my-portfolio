from app import app

from flask import render_template

common = {
    'first_name': 'Mateusz',
    'last_name': 'Guła',
    'alias': 'gua'
}

@app.route('/')
def index():
    return render_template('home.html', common=common)


