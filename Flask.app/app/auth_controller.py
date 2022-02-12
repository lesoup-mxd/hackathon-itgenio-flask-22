from flask_login.utils import login_required
from app import app, db, index
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, current_user
from models.user import User
from forms.login_form import LoginForm
from flask_login import login_user, logout_user
from werkzeug.urls import url_parse
from flask import request
from forms.registration_form import RegistrationForm 


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!')
        return redirect(url_for('login'))
    return render_template(
        'auth/registration.html',
        title='Register',
        form=form
    )

@app.route('/auth/logout/')
@app.route('/logout/')
@login_required
def logout():
    login_user()
    flash("You have logged out")
    return redirect(url_for('login'))

@app.route('/login/', methods=['post', 'get'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
     
        flash("Wrong username or password", "error")
        return redirect(url_for('login'))
    return render_template('auth/login.html', form=form)
