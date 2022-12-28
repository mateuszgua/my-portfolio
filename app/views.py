import os
import io
import json

from app import app

from flask import render_template, request

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
