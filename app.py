import os
import random
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from answers import answers_pool as answers

app = Flask(__name__)

# get directory of file
basedir = os.path.abspath(os.path.dirname(__file__))
# create path to sqlite file based on directory path above
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# wrap flask-alchemy instance around flask app
db = SQLAlchemy(app)

# MODELS
class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question_body = db.Column(db.String(64))
    answer_body = db.Column(db.String(64))

    def __repr__(self):
        return '<Question %r - %r>' % self.question_body, self.answer_body

# SET UP DATABASE
db.drop_all()
db.create_all()
# sample questions and answers
questions = ['Will I pass?', 'Will lockdown end soon?']
for question in questions:
    answer = random.choice(answers)
    new_question_entry = Question(question_body=question, answer_body=answer)
    db.session.add(new_question_entry)
db.session.commit()


# ROUTES
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/add_question', methods=['POST'])
def add_question():
    question = request.form.get('questionBody')
    answer = random.choice(answers)
    new_question_entry = Question(question_body=question, answer_body=answer)
    db.session.add(new_question_entry)
    db.session.commit()
    return redirect(url_for('answer'))

@app.route('/answer')
def answer():
    last_question = Question.query.order_by(Question.id.desc()).first()
    return render_template("answer.html", most_recent_question=last_question)


@app.route('/allquestions')
def show_all_questions():
    questions = Question.query.all()
    return render_template("allquestions.html", questions=questions)




