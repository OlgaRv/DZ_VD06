from flask import render_template, request, redirect, url_for
from app import app

profiles = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        town = request.form.get('town')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        if username and town and hobby and age:
            profiles.append({'username': username, 'town': town, 'hobby': hobby, 'age': age})
            return redirect(url_for('index'))
    return render_template('anketa.html', profiles=profiles)

