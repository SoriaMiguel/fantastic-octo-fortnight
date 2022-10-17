from flask import Flask
from markupsafe import escape
from flask import request
from flask import redirect, url_for
from seeds import seed

app = Flask(__name__)

users = seed.users
experiences = seed.experiences
ids = seed.ids

@app.get("/candidate/list")
def show_candidate_list():
    return users

@app.route("/candidate/<string:candidate_id>",  methods=["GET", "POST"])
def candidate(candidate_id):
    if candidate_id in ids:
        candidate = next((user for user in users if user["id"] == candidate_id), None)
        candidate_experiences = []
        for experience in experiences:
            if experience["id"] == candidate_id:
                candidate_experiences.append(experience)

        candidate["experience"] = candidate_experiences

        if request.method == "GET":
            return candidate
        if request.method == "POST":
            if request.args.get("name", "") != "": candidate["name"] = request.form["name"]
            if request.args.get("bio", "") != "": candidate["bio"] = request.form["bio"]
            if request.args.get("picture", "") != "": candidate["picture"] = request.form["picture"]

            # doing in memory returns experiences on GET after candidate is modified or retreived
            return candidate
            # or redirect to GET /candidate/candidate_id?
    else:
        # raise error/handle error
        return f"Could not find candidate: {escape(candidate_id)}"
