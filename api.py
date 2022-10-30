from flask import Flask, jsonify
from activities.brain_gym_data import activities
from activities.wellbeing_data import wellb_activities

app = Flask(__name__)


@app.route('/activity')
def get_activities():
    return jsonify(activities)


# @app.get("/")
# def activity_list():
#     random_activity = get_activities()
#     return render_template("activity_list.html", random_activity=random_activity)


@app.route('/activity/<int:aid>')
def get_activity_id(aid):
    return [item for item in activities if item['id'] == aid]


@app.get("/activity/<activity_name>")
def activity_name_data(activity_name):
    return [item for item in activities if item['name'] == activity_name]
    # return f"This is {activities['name'].capitalize()}.\n" \
    #        f"Duration: {activities['duration']}.\n" \
    #        f"Benefits: {activities['benefits']}.\n" \
    #        f"You Tube Video Link: {activities['link']}.\n"


# @app.route("/activity/<int:duration>")
# def activity_duration_data(activity_duration):
#     return [item for item in activity if item['duration'] == activity_duration]

@app.route('/wellbeing')
def get__wellb_activities():
    return jsonify(wellb_activities)


# @app.get("/")
# def activity_list():
#     random_activity = get_activities()
#     return render_template("activity_list.html", random_activity=random_activity)


@app.route('/wellbeing/<int:wid>')
def get_wellb_activity_id(wid):
    return [item for item in wellb_activities if item['id'] == wid]


@app.get("/wellbeing/<activity_name>")
def wellb_activity_name_data(wellb_activity_name):
    return [item for item in activities if item['name'] == wellb_activity_name]
    # return f"This is {wellb_activities['name'].capitalize()}.\n" \
    #        f"Duration: {wellb_activities['duration']}.\n" \
    #        f"Activity To Do: {wellb_activities['activity']}.\n"


# @app.route("/activity/<int:duration>")
# def activity_duration_data(activity_duration):
#     return [item for item in activity if item['duration'] == activity_duration]



if __name__ == "__main__":
    app.run(port=8009)
