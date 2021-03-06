from flask import Flask, render_template, request, redirect, url_for
import create_db
import leaderboard_db
import os
import config
import edit_db

app = Flask(__name__)

if os.path.isfile(config.db_filename) == False:
    create_db.create_db()

@app.route('/home', methods=['GET'])
def home():
    users = leaderboard_db.get_users()
    leaderboards = leaderboard_db.get_leaderboards()

    return render_template('home.html', users=users, leaderboards=leaderboards)

@app.route('/<username>', methods=['GET'])
def user(username):
    users = leaderboard_db.get_users()
    leaderboards = leaderboard_db.get_leaderboards()

    return render_template('user.html', username=username, users=users, leaderboards=leaderboards)

@app.route('/<username>/<id>', methods=['GET'])
def view(username, id):
    users = leaderboard_db.get_users()
    leaderboards = leaderboard_db.get_leaderboards()

    return render_template('view_leaderboard.html', username=username, users=users, leaderboards=leaderboards)

@app.route('/new-leaderboard', methods=['GET', 'POST'])
def newLeaderboard():
    if request.method == "POST":
        edit_db.add_leaderboard(request.form['titleLeaderboard'], request.form['description'], request.form['genre'], request.form['author'])
        return redirect(url_for('home'))
    else:
        return render_template('new_leaderboard.html')

app.run(host='127.0.0.2', port='8080', debug=True)