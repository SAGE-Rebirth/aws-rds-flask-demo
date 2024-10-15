# application/routes.py
from flask import render_template, request
from application import app, db
from application.models import User
from application.forms import UserForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
    users = User.query.order_by(User.id.desc()).limit(5).all()
    return render_template('index.html', form=form, users=users)
