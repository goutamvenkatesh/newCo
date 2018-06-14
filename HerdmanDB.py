from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:mzLapq23@localhost:1433/HerdmanData?driver=SQL+Server'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://sa:mzLapq23@localhost:1433/HerdmanData'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


class Breed(db.Model):
    __tablename__ = 'Common.Breed'
    SpeciesCode = db.Column('Speciescode', db.Integer, primary_key=True)
    BreedCode = db.Column('BreedCode', db.Integer)
    Name = db.Column('Name', db.Unicode)
    BreedType = db.Column('BreedType', db.Unicode)
    SyncID = db.Column('SyncID', db.Integer)

# class Treatment(db.Model):
#     __tablename__ = db.Model.metadata.tables['Account.Deduction']


@app.route("/")
@app.route("/home")
def home():
    # return "<h1>Hello World!</h1>"
    return render_template('home.html')

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

SQLALCHEMY_TRACK_MODIFICATIONS = False



if __name__ == '__main__':
    app.run(debug=True)