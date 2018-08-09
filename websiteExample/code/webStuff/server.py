from flask import Flask, render_template, url_for, request
import os
import csv

app = Flask(__name__)

def readtextfile(x):
    Teams = {}
    with open('static/Games/Week'+str(x)+'Bare.out','r') as inf:
        Teams = eval(inf.read())
    return Teams

@app.route("/Football_week_1")
def Football_week_1():
    Teams = readtextfile("1")
    x = int(100)
    return render_template("football.html", Teams=Teams, x=x)


@app.route("/Football_week_2")
def Football_week_2():
    Teams = readtextfile("2")
    x = int(100)
    return render_template("football.html", Teams=Teams, x=x)


@app.route("/Football_week_3")
def Football_week_3():
    Teams = readtextfile("3")
    x = int(100)
    return render_template("football.html", Teams=Teams, x=x)

@app.route("/Football_week_4")
def Football_week_4():
    Teams = readtextfile("4")
    x = int(100)
    return render_template("football.html", Teams=Teams, x=x)

@app.route("/Football_week_5")
def Football_week_5():
    Teams = readtextfile("5")
    x = int(100)
    return render_template("football.html", Teams=Teams, x=x)

@app.route("/Football_week_6")
def Football_week_6():
    Teams = readtextfile("6")
    x = int(100)
    return render_template("football.html", Teams=Teams, x=x)

@app.route("/Football_week_7")
def Football_week_7():
    Teams = readtextfile("7")
    x = int(100)
    return render_template("football.html", Teams=Teams, x=x)

'''
steelers,panthers
bengals,saints
browns,falcons
packers,dolphins
colts,jaguars
bears,lions
chiefs,cardinals
jets,bills
buccaneers,redskins
titans,patriots
raiders,chargers
rams,seahawks
eagles,cowboys
49ers,giants
'''
@app.route('/', methods=['GET', 'POST'])
def index():
	print("Someone is at the home page.")
	return render_template('Homepage.html')

@app.route('/my-link/')
def my_link():
	print('I got clicked!')
	return 'Click.'
'''
@app.route('/results/', methods=['GET', 'POST'])
def results():
	if request.method == 'POST':
		data = request.form
	else:
		data = request.args

	query = data.get('searchterm')
	print("You searched for: " + query)
	firstName = ['Ben','Sarah', 'Xandar', 'Ellewyn']
	lastName = ['McCamish', 'G', 'Quazar', 'Sabbeth']
	return render_template('results.html', query=query, results=zip(firstName, lastName))
'''
#Found at URL: http://flask.pocoo.org/snippets/40/
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
	app.run(debug=True)
