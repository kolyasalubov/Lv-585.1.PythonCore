from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from datetime import date

hosp = Flask(__name__)
hosp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Taras1taras1@localhost:3306/hospital'
hosp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(hosp)

class Departments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    beds_number = db.Column(db.Integer, nullable = False, default = 0)
    pat_admission = db.relationship('Patients', backref = "admission_place", lazy = True)
    employment = db.relationship('Physicians', backref = "employer", lazy = True)

    def __repr__(self):
        return f"<Department {self.id}>"

class Patients(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(30), nullable = False)
    lastname = db.Column(db.String(30), nullable = False)
    birth_date = db.Column(db.Date, nullable = False)
    sex = db.Column(db.String(6), nullable = False)
    diagnosis = db.Column(db.String(200), nullable = False)
    admission_date = db.Column(db.Date, nullable = False)
    discharge_date = db.Column(db.Date, nullable = False)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable = False)
    physician_id = db.Column(db.Integer, db.ForeignKey("physicians.id"), nullable = False)    

    def __repr__(self):
        return f"<Patient {self.id}>" 

class Physicians(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(30), nullable = False)
    lastname = db.Column(db.String(30), nullable = False)
    subspeciality = db.Column(db.String(30), nullable = False)
    position = db.Column(db.String(30), nullable = False)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable = False)
    treatment_pair = db.relationship('Patients', backref = "doctor", lazy = True)
    
    def __repr__(self):
        return f"<Physician {self.id}>" 

@hosp.route("/", methods = ("POST", "GET"))
def index():
    return render_template("index.html", title = "Головна")

@hosp.route("/departments", methods = ("POST", "GET"))
def departments_reg():
    if request.method == "POST":
        try:
            d = Departments(name=request.form['name'], beds_number=request.form['beds_number'])      
            db.session.add(d)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print("Помилка введення даних в БД")

        return redirect(url_for('index'))
    return render_template("departments.html", title = "Відділення")

@hosp.route("/patients", methods = ("POST", "GET"))
def patients_reg():
    if request.method == "POST":
        try:
            p = Patients(firstname=request.form['firstname'], lastname=request.form['lastname'], birth_date=request.form['birth_date'],
                        sex=request.form['sex'], diagnosis=request.form['diagnosis'], admission_date=request.form['admission_date'],
                        discharge_date=request.form['discharge_date'], department_id=request.form['department_id'],
                        physician_id=request.form['physician_id'])
            db.session.add(p)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print("Помилка введення даних в БД")
        return redirect(url_for('index'))
    return render_template("patients.html", title = "Пацієнти")

@hosp.route("/physicians", methods = ("POST", "GET"))
def physicians_reg():
    if request.method == "POST":
        try:
            ph = Physicians(firstname=request.form['firstname'], lastname=request.form['lastname'], subspeciality=request.form['subspeciality'],
                        position=request.form['position'], department_id=request.form['department_id'])  
            db.session.add(ph)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print("Помилка введення даних в БД")

        return redirect(url_for('index'))
    return render_template("physicians.html", title = "Лікарі")

if __name__ == "__main__":
    hosp.run(debug = True)
    