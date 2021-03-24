from werkzeug.urls import url_parse
from werkzeug.utils import redirect
from app import app, db
from flask import render_template, request, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import RegistrationForm, LoginFrom
from app.model import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('cart.html', title='home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(userId=form.userId.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid username or password')
        else:
            login_user(user, form.remember_me.data)

        # 重定向到登录页面
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(userId=form.userId.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
