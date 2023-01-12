import json

from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_mail import Message

from app import app, form, mail
from app.helpers import Helper


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')


@app.route('/timeline', methods=['GET'])
def timeline():
    return render_template('timeline.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@app.route('/user', methods=['GET'])
def user():
    with open("app/static/files/user.json", "r") as f:
        data = json.load(f)
    if request.method == 'GET':
        return jsonify(data)


@app.route('/technologies', methods=['GET'])
def technologies():
    with open("app/static/files/technologies.json", "r") as f:
        data = json.load(f)
    if request.method == 'GET':
        return jsonify(data)


@app.route('/projects/load', methods=["GET"])
def projects_load():
    with open("app/static/files/projects.json", "r") as f:
        data = json.load(f)
    data.sort(key=Helper.order_projects_by_weight, reverse=True)
    if request.method == 'GET':
        return jsonify(data)


@app.route('/timeline/load', methods=["GET"])
def timeline_load():
    with open("app/static/files/timeline.json", "r") as f:
        data = json.load(f)
    if request.method == 'GET':
        return jsonify(data)
