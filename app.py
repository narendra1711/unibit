from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import sqlite3 as sql
from user_validation import f_user_validation
from user_registration import f_user_registration
from business_checks_insertion import f_business_checks
from data_checks_insertion import f_data_checks
from on_boarding import f_on_boarding
from data_api import f_data_api
from log_details import f_log_details
import settings

# Application Initialization
app = Flask(__name__)
db_name = settings.db_name
app.secret_key = "thisissecretkey"

# Rendering HTML Pages
######################
# index.html
@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template("index.html")

# signup.html
@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    return render_template("sign_up.html")

# signin.html
@app.route('/signin', methods = ['POST', 'GET'])
def signin():
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
def logs():
    return render_template("logs.html")

# data api.html
@app.route('/data_api', methods = ['POST', 'GET'])
def data_api():
    return render_template("data_api.html")

# user onboarding.html
@app.route('/onboard', methods = ['POST', 'GET'])
def onboard():
    return render_template("on_boarding.html")

# user validation logic
@app.route('/validation', methods = ['POST', 'GET'])
def validation():
    if request.method == 'POST':
        user = request.form['user_name']
        password = request.form["password"]
        data, login_flag = f_user_validation(user, password, db_name)
        if login_flag:
            return redirect(url_for('dashboard'))    

# user registration logic         
@app.route('/registration', methods = ['POST', 'GET'])
def registration():
    if request.method == 'POST':
        user = request.form['user_name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            data = f_user_registration(user, password, db_name)
        else:
            data = "Re-Enter Password"
        return jsonify({'data':data})

# business checks logic
@app.route('/b_checks', methods = ['POST', 'GET'])
def b_checks():
    if request.method == 'POST':
        module_name = request.form['module_name']
        process_name = request.form['process_name']
        query = request.form['query']
        notify_email = request.form['notify_email']
        data = f_business_checks(module_name, process_name, query, notify_email, db_name)
        return jsonify({'data':data})

# data checks logic
@app.route('/d_checks', methods = ['POST', 'GET'])
def d_checks():
    if request.method == 'POST':
        module_name = request.form['module_name']
        process_name = request.form['process_name']
        query = request.form['query']
        notify_email = request.form['notify_email']
        data = f_data_checks(module_name, process_name, query, notify_email, db_name)
        return jsonify({'data':data})

# generate logs logic
@app.route('/generate_logs')
def generate_logs():
    return jsonify({'data': f_log_details(db_name)})

# data api logic
@app.route('/user_data_api', methods = ['POST', 'GET'])
def user_data_api():
    if request.method == 'GET':
        db_name = "unibit.db"
        query = "SELECT * FROM LOG_DETAILS;"
        data = f_data_api(db_name, query)
        return jsonify({'data':data})

# user onboarding logic
@app.route('/user_onboard', methods = ['POST', 'GET'])
def user_onboard():
    if request.method == 'POST':
        use_case_name = request.form['use_case_name']
        use_case_admin = request.form['use_case_admin']
        desc = request.form['desc']
        data = f_on_boarding(use_case_name, use_case_admin, desc, db_name)
        data = "User On-Boarding Submitted"
        return jsonify({'data':data})

# run application
if __name__ == '__main__':
   app.run(debug = True)