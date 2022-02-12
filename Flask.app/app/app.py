from flask import Flask, render_template
from question import Question
from forms import QuestionForm
from flask import url_for
from flask import redirect
from werkzeug.utils import secure_filename
from config import Config
from flask import abort, request


app = Flask(__name__)
app.config.from_object(Config)

all_questions = {}

@app.route('/questions/question<int:id>')
def question(id):
    q = all_questions[id]
    if not q:
        return abort(404)
    return render_template(f'questions/question.html', question=q, title=f'{q.name} - {q.author}')

@app.route("/questions")
def questions():
    return render_template('questions/index.html', questions=all_questions, title='Questions')

@app.route('/question/create', methods=['GET', 'POST'])
def create_question():
    form = QuestionForm()
    if form.validate_on_submit():
        filename = ''

        new_question = Question(name = form.name.data, author= form.author.data, theQuestion= form.theQuestion.data, answer= form.answer.data)
        all_questions[new_question.id] = new_question
        return redirect(url_for('questions'))
        
    return render_template('questions/question_form.html', form=form, action_name='Create')


@app.route('/questions/<int:id>/edit', methods=['GET', 'POST'])
def edit_question(id):
    form = QuestionForm()
    
    editable_question = all_questions.get(id)

    if form.validate_on_submit():
        editable_question.name = form.name.data
        editable_question.author = form.author.data
        editable_question.theQuestion = form.theQuestion.data
        editable_question.answer = form.answer.data
        return redirect(url_for('questions'))
    

    form.name.data = editable_question.name
    form.theQuestion.data = editable_question.genre
    form.answer.data = editable_question.description
    form.author.data = editable_question.author
    return render_template('questions/question_form.html', form=form,
                           action_name='Edit', question_id=id)


@app.route('/questions/<int:id>/remove', methods=['GET', 'POST'])
def remove_question(id):
    removable_question = all_questions.get(id)

    if request.method == 'POST':
        del all_questions[id]
        return redirect(url_for('questions'))
    return render_template('questions/remove_question.html', question=removable_question)