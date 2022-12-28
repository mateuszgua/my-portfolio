import os
import io
import json

from flask import render_template, request, flash, redirect, url_for
from flask_mail import Message

from app import app, form, mail


common = {
    'first_name': 'Mateusz',
    'last_name': 'Guła',
    'alias': 'gua'
}


@app.route('/')
def index():
    return render_template('home.html', common=common)


@app.route('/projects')
def projects():
    data = get_static_json("static/projects/projects.json")['projects']
    data.sort(key=order_projects_by_weight, reverse=True)

    tag = request.args.get('tags')
    if tag is not None:
        data = [project for project in data if tag.lower() in [project_tag.lower()
                                                               for project_tag in project['tags']]]

    return render_template('projects.html', common=common, projects=data, tag=tag)


def order_projects_by_weight(projects):
    try:
        return int(projects['weight'])
    except KeyError:
        return 0


def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)


def get_static_json(path):
    return json.load(open(get_static_file(path)))


@app.route('/timeline')
def timeline():
    data = get_static_json("static/files/timeline.json")
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
