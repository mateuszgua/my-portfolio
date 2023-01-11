import json

from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_mail import Message

from app import app, form, mail
from app.helpers import Helper


@app.route('/', methods=['GET', 'POST'])
def index():
    with open("app/static/files/user.json", "r") as f:
        data = json.load(f)
    if request.method == 'GET':
        return jsonify(data)


@app.route('/projects', methods=["GET"])
def projects():
    with open("app/static/files/projects.json", "r") as f:
        data = json.load(f)
    data.sort(key=Helper.order_projects_by_weight, reverse=True)
    if request.method == 'GET':
        return jsonify(data)


@app.route('/timeline', methods=["GET"])
def timeline():
    with open("app/static/files/timeline.json", "r") as f:
        data = json.load(f)
    if request.method == 'GET':
        return jsonify(data)


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
