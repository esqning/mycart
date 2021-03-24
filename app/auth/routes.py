from werkzeug.urls import url_parse
from werkzeug.utils import redirect
from app import db
from flask import render_template, request, url_for, flash
from flask_login import current_user, login_user, logout_user
from . import auth
from .forms import RegistrationForm, LoginFrom
from app.model import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
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
            next_page = url_for('main.index')
        return redirect(next_page)

    return render_template('auth/login.html', title='login', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(userId=form.userId.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form)
