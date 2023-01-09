import json

from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_mail import Message

from app import app, form, mail
from app.helpers import Helper

common = {
    'test1': 'test2'
}


@app.route('/')
def index():
    message = {'greeting': 'Hello from Flask!'}
    return jsonify(message)  # serialize and use JSON headers
    # return render_template('home.html', common=common)


@app.route('/user', methods=['GET', 'POST'])
def user():
    message = {
        "first_name": "MATEUSZ",
        "last_name": "GUŁA",
        "nick": "gua",
        "field": "Junior Backend Developer",
        "description": "I am engineer who is been trying his hand at backend for some time now. My last position allowed me start my programming adventure. Since then I have developed my database and web development abilities. I like solving the problems and analytical thinking. I amhardworking and multitasking. I am open mindset to learn new technologies. I feel great at teamwork. In my free time I am interested in sport and new technologies. Also I like play board games."
    }
    if request.method == 'GET':
        return jsonify(message)


@app.route('/users', methods=["GET"])
def users():
    print("users endpoint reached...")
    with open("users.json", "r") as f:
        data = json.load(f)
        data.append({
            "username": "user4",
            "pets": ["hamster"]
        })
        return jsonify(data)


@app.route('/projects')
def projects():
    data = Helper.get_static_json("static/projects/projects.json")['projects']
    data.sort(key=Helper.order_projects_by_weight, reverse=True)

    tag = request.args.get('tags')
    if tag is not None:
        data = [project for project in data if tag.lower() in [project_tag.lower()
                                                               for project_tag in project['tags']]]

    return render_template('projects.html', common=common, projects=data, tag=tag)


@app.route('/timeline')
def timeline():
    data = Helper.get_static_json("static/files/timeline.json")
    return render_template('timeline.html', common=common, timeline=data)


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    contact_form = form.ContactForm()
    if request.method == 'POST':
        if contact_form.validate_on_submit:
            name = request.form["name"]
            email = request.form["email"]
            subject = request.form["subject"]
            message = request.form["message"]
            msg = Message(subject=subject, body=message,
                          sender=email, recipients=['my_mail@gmail.com'])
            mail.send(msg)
        else:
            flash('All fields are required.')

        return redirect(url_for('contact'))
    else:
        return render_template('contact.html', form=contact_form)
