from flask import Flask, jsonify, render_template

app = Flask(__name__)

chart = {
    'labels': ['Tue', 'Wed', 'Thu', 'Fri', 'Sat',
               'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue'],
    'series': [2, 6, 2, 4, 0, 0, 3, 2, 1, 0, 0, 0, 3, 6, 1]
}


# print(jsonify(chart))

@app.route('/')
def index():
    # print(open("templates/index.html","r",encoding="utf8"))
    # return 'Hello, world!'
    return render_template("index.html")


@app.route('/api/')
def chart():
    t = {
        'labels': ['Tue', 'Wed', 'Thu', 'Fri', 'Sat',
                   'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue'],
        'series': [2, 6, 2, 4, 0, 0, 3, 2, 1, 0, 0, 0, 3, 6, 1]
    }
    return jsonify(t)


if __name__ == '__main__':
    app.run(debug=True)
