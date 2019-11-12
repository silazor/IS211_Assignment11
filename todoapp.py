from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import re

app = Flask(__name__)

my_list = []

@app.route('/')
def route_one():
    return render_template('index.html', my_list = my_list)

@app.route('/submit', methods = ['POST','GET'])
def route_two():
    if request.method == 'POST':
        email = request.form['email']
        task = request.form['task']
        priority = request.form['priority']
        error = ''

        # validate the email
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if( not re.search(regex,email)):
            error = "ERROR: Invalid email!"
            return render_template('index.html', my_list = my_list, error = error)

        # Validate the priority
        print(priority)
        if priority != 'low' and  priority != 'medium' and priority != 'high':
            error = "ERROR: Invalid Priority!"
            return render_template('index.html', my_list = my_list, error = error)

        my_list.append([email, priority, task])
    return redirect(url_for('route_one'))

@app.route('/clear', methods = ['POST', 'GET'])
def route_three():
    #if request.method == 'POST':
    my_list.clear()

    return redirect(url_for('route_one'))

if __name__ == '__main__':
    app.run(debug = True)
