from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/home_page")
def home_page():
    return redirect(url_for('index_page'))

@app.route("/professional")
def professional_page():
    return render_template('cv.html')

@app.route("/cv")
def cv_page():
    return redirect('/professional')

@app.route("/Assignment8")
def Assignment8_page():
    name = 'Carmel'
    last_name = 'Ben Shoshan'
    return render_template('Assignment8.html',
                           name=name,
                           last_name=last_name,
                           profile={'Favorite hobbie': 'to take pictures',
                                    'Favorite music': 'Harry Styles',
                                    'Favorite place': 'Home'})


if __name__ == '__main__':
    app.run(debug=True)