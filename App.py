from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

users = {'user1': {'name': 'Yossi', 'email': 'yo@gmail.com'},
         'user2': {'name': 'Carmel', 'email': 'carmel@gmail.com'},
         'user3': {'name': 'Lior', 'email': 'lior@hotmail.com'},
         'user4': {'name': 'Noam', 'email': 'noam@yahoo.com'},
         'user5': {'name': 'ofir', 'email': 'ofir@mail.com'},
         'user6': {'name': 'ofer', 'email': 'ofer@gmail.com'}
         }


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



@app.route("/assignment9", methods=['GET', 'POST'])
def assignment9_page():
    # search form
    if 'email' in request.args:
        email = request.args['email']
        if email == '':
            return render_template('assignment9.html', user_list=users)
        # search it in users dict
        for key, value in users.items():
            if value.get('email') == email:
                return render_template('assignment9.html', u_name=value.get('name'), u_email=value.get('email'))
    # registration form
    if request.method == "POST":
        session['username'] = request.form['username']
    return render_template('assignment9.html')

@app.route("/logout", methods=['GET', 'POST'])
def logout_func():
    session['username'] = ''
    return render_template('assignment9.html')


if __name__ == '__main__':
    app.secret_key = '123'
    app.run(debug=True)