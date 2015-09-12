from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from datetime import date

# local configs
from localsettings import VERSION
from localsettings import BIRTHDAYS

app = Flask(__name__)

@app.route("/")
def index_route(params={}):
    today = date.today()
    today_index = (today.month, today.day)
    today_birthdays = BIRTHDAYS.get(today_index)
    year = today.year
    birthdays = []
    birthday_postfixes = {
        0: "th",
        1: "st",
        2: "nd",
        3: "rd",
        4: "th",
        5: "th",
        6: "th",
        7: "th",
        8: "th",
        9: "th",
    }

    if today_birthdays != None:
        for birthday in today_birthdays:
            if birthday.get('year') != None:
              birthday['age'] = year - birthday['year']
              birthday['postfix'] = birthday_postfixes[birthday['age'] % 10]

        birthdays = today_birthdays

    return render_template("index.html", params = {
      "version": VERSION,
      "birthdays": birthdays
    })

@app.route("/version")
def version_route():
    data = {}
    data["version"] = VERSION

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)