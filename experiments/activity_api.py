'''coode to run the activities data as an external api so data is stored externally'''

from flask import Flask, jsonify
from experiments.activities_data import all_activities

app = Flask(__name__)


@app.route('/activity')
def get_activities():
    return jsonify(all_activities)


@app.route('/activity/<int:aid>')
def get_activity_id(aid):
    return [item for item in all_activities if item['id'] == aid]


@app.get("/activity/<activity_name>")
def activity_name_data(activity_name):
    return [item for item in all_activities if item['name'] == activity_name]

if __name__ == "__main__":
    app.run(port=8009)
