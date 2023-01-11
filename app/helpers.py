import os
import json


class Helper:

    def order_projects_by_weight(projects):
        try:
            return int(projects['weight'])
        except KeyError:
            return 0

    def get_static_json(path):
        return json.load(open(get_static_file(path)))


def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)
