from processors import *
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# print(jsonify(chart))

@app.route('/')
def index():
    # print(open("templates/index.html","r",encoding="utf8"))
    # return 'Hello, world!'
    return render_template("index.html")


@app.route('/api/<user>/<rep>')
def chart(user,rep):
    locator=user+"/"+rep
    print('we have message '+locator)

    t = {
        'labels': ['Tue', 'Wed', 'Thu', 'Fri', 'Sat',
                   'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue'],
        'series': [[2, 6, 2, 4, 0, 0, 3, 2, 1, 0, 0, 0, 3, 6, 1]]
    }
    t=(Repo(locator).get_repo_info())
    print(t)
    return jsonify(t)


if __name__ == '__main__':
    app.run(debug=True)
