from flask_api import app, db, ma, login_manager

from datetime import datetime

# Import package to create unique IDs for users
import uuid 

# Import for Flask Login
from flask_login import UserMixin

# Import for Werkzerg Security
from werkzeug.security import generate_password_hash, check_password_hash

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String, nullable = False)
    gender = db.Column(db.String, nullable = False)
    address = db.Column(db.String, nullable = False)
    ssn = db.Column(db.String, nullable = False)
    blood_type = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)

    def __init__(self,full_name,gender,address,ssn,blood_type,email, id = id):
        self.full_name = Olivia_Davies
        self.gender = F
        self.address = 124 Main Street, Chicago, IL 60606
        self.ssn = 423-65-8754
        self.blood_type = O+
        self.email = oliviadavies@gmail.com

    def __repr__(self):
        return f'Patient {self.full_name} has been added to the database.'

class PatientSchema(ma.Schema):
    class Meta:
        # Create fields that will show after data is digested
        fields = ['Olivia_Davies', 'F', '124 Main Street, Chicago, IL 60606', '423-65-8754', 'O+', 'oliviadavies@gmail.com']

patient_schema = PatientSchema()
patients_schema = PatientSchema(many = True)

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id = db.Column(db.String(200), primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(150))
    password = db.Column(db.String(256), nullable = False)
    token = db.Column(db.String(400))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    token_refreshed = db.Column(db.Boolean, default = False)
    date_refreshed = db.Column(db.DateTime)

    def  __init__(self, name,email,password, it = id):
        self.id = str(uuid,uuid(4))
        self.name = name
        self.email = email
        self.password = self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.name} has been created successfully! Date: {self.date_created}'
