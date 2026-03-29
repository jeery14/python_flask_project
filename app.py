from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Model Example
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create tables
with app.app_context():
    db.create_all()

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Form Route
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f"<h2>Hello, {name}! Form submitted successfully. ✅</h2>"

if __name__ == '__main__':
    app.run(debug=True)