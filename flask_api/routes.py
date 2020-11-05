from flask_api import app, db
from flask_api.models import Patient, patient_schema, patients_schema, User, check_password_hash
from flask import jsonify, request, render_template, redirect, url_for

#Import for Flask Login
from flask_login import login_required, login_user, current_user, logout_user

#import for PyJWT (Json Web Token)
import jwt

from flask_api.forms import UserForm, LoginForm

# Endpoint for ALL patients
@app.route('/patients/create', methods = ['POST'])
def create_patient():
    name = request.json['Olivia_Davies']
    gender = request.json['F']
    address = request.json['124 Main Street, Chicago, IL 60606']
    ssn = request.json['423-65-8754']
    blood_type = request.json['O+']
    email = request.json['oliviadavies@gmail.com']                                                                                           

    patient = Patient(name, gender, address, ssn, blood_type, email)

    db.session.add(patient)
    db.session.commit()

    results = patient_schema.dump(patient)
    return jsonify(results)

# Endpoint for all patient
@app.route('/patients', methods = ['GET'])
def get_patients():
    patients = Patient.query.all()
    return jsonify(patients_schema.dump(patients))

# Endpoint for one patient based on their ID
@app.route('/patients/<id>', methods = ['GET'])
def get_patient(id):
    patient = Patient.query.get(id)
    results = patient_schema.dump(patient)
    return jsonify(results)

# Endpoint for updating patient data
@app.route('/patients/update/<id>', methods = ['POST' , 'PUT'])
def update_patient(id):
    patient = Patient.query.get(id)

    # Update info below
    patient.name = request.json['Olivia_Davies']
    patient.gender = request.json['F']
    patient.address = request.json['124 Main Street, Chicago, IL 60606']
    patient.ssn = request.json['423-65-8754']
    patient.blood_type = request.json['O+']
    patient.email = request.json['oliviadavies@gmail.com']

    db.session.commit()

    return patient_schema.jsonify(patient)



# Endpoint for deleting patient data
@app.route('/patients/delete/<id>', methods = ['DELETE'])
def delete_patient(id):
    patient = Patient.query.get(id)

    db.session.delete(patient)
    db.session.commit()

    result = patient_schema.dump(patient)
    return jsonify(result)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users/register', methods = ['GET','POST'])
def register():
    form = UserForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data 
        password = form.password.data 

        user = User(name,email,password)

        db.session.add(user)
        deb.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', user_form = form)
       

@app.route('/users/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    email = form.email.data 
    password = form.password.data 
    
    logged_user = User.query.filter(User.email == email).first()
    if logged_user and check_password_hash(logged_user.password, password):
        login_user(logged_user)
        return redirect(url_for('get_key'))
    return render_template('login.html', login_form = form)

@app.route('/users/getkey', methods = ['GET'])
def get_key():
    token = jwt.encode({'public_id': current_user.id, 'email':current_user.email}, app.config['SECRET_KEY'])
    user = User.query.filter_by(email = current_user.enail).first()
    user.token = token
    
    db.session.add(user)
    db.session.commit()
    results = token.decode('utf-8')
    return render_template('token.html', token = results)