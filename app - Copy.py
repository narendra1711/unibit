from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3 as sql
from user_validation import user_validation
from user_registration import user_registration
from business_checks_insertion import business_checks_insertion
from data_checks_insertion import data_checks_insertion
from on_boarding import on_boarding
from data_api import data_api
from log_details import log_details
import settings

# Application Initialization
app = Flask(__name__)
db_name = settings.db_name

# Rendering HTML Pages
######################
# index.html
@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template("index.html")

# signup.html
@app.route('/signup', methods = ['POST', 'GET'])
def sign_up():
    return render_template("sign_up.html")

# signin.html
@app.route('/signin', methods = ['POST', 'GET'])
def sign_in():
    return render_template("sign_in.html")

# dashboard.html
@app.route('/dashboard', methods = ['POST', 'GET'])
def dashboard():
    return render_template("dashboard.html")

# business checks.html
@app.route('/business_checks', methods = ['POST', 'GET'])
def business_checks():
    return render_template("business_checks.html")

# data checks.html
@app.route('/data_checks', methods = ['POST', 'GET'])
def data_checks():
    return render_template("data_checks.html")

# log.html
@app.route('/logs', methods = ['POST', 'GET'])
def log_data():
    return render_template("logs.html")

# data api.html
@app.route('/data_api', methods = ['POST', 'GET'])
def api():
    return render_template("data_api.html")

# user onboarding.html
@app.route('/user_onboarding', methods = ['POST', 'GET'])
def on_board():
    return render_template("on_boarding.html")



@app.route('/user_validation', methods = ['POST', 'GET'])
def authentication():
    if request.method == 'POST':
        user = request.form['user_name']
        password = request.form["password"]
        print(user)
        data, login_flag = user_validation(user, password, db_name)
        if login_flag:
            return redirect(url_for('dashboard'))    
         
@app.route('/user_registration', methods = ['POST', 'GET'])
def registration():
    if request.method == 'POST':
        user = request.form['user_name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            data = user_registration(user, password, db_name)
        else:
            data = "Re-Enter Password"
        return jsonify({'data':data})

@app.route('/on_boarding', methods = ['POST', 'GET'])
def onboarding():
    if request.method == 'POST':
        use_case_name = request.form['use_case_name']
        use_case_admin = request.form['use_case_admin']
        desc = request.form['desc']
        data = on_boarding(use_case_name, use_case_admin, desc, db_name)
        data = "User On-Boarding Submitted"
        return jsonify({'data':data})

@app.route('/b_checks', methods = ['POST', 'GET'])
def b_checks():
    if request.method == 'POST':
        print("Inside:")
        module_name = request.form['module_name']
        process_name = request.form['process_name']
        query = request.form['query']
        notify_email = request.form['notify_email']
        print(module_name, process_name, query, notify_email, db_name)
        data = business_checks_insertion(module_name, process_name, query, notify_email, db_name)
        print(data)
        return jsonify({'data':data})

@app.route('/d_checks', methods = ['POST', 'GET'])
def d_checks():
    if request.method == 'POST':
        print("Inside:")
        module_name = request.form['module_name']
        process_name = request.form['process_name']
        query = request.form['query']
        notify_email = request.form['notify_email']
        print(module_name, process_name, query, notify_email, db_name)
        data = data_checks_insertion(module_name, process_name, query, notify_email, db_name)
        print(data)
        return jsonify({'data':data})

@app.route('/log_details')
def log_table_data():
    data = log_details(db_name)
    return jsonify({'data':data})

@app.route('/data_api_route', methods = ['POST', 'GET'])
def data():
    print("Hllo")
    if request.method == 'GET':
        db_name = "unibit.db"
        query = "SELECT * FROM LOG_DETAILS;"
        data = data_api(db_name, query)
        print(data)
        return jsonify({'data':data})

if __name__ == '__main__':
   app.run(debug = True)